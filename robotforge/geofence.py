"""Synthetic geofence decision engine; no GPS coordinates or child data collected."""
from dataclasses import dataclass
from math import isfinite

FEET_TO_METERS = 0.3048


@dataclass(frozen=True)
class Sample:
    """Synthetic distance from anchor, reported uncertainty and update age in seconds."""
    distance_m: float
    accuracy_m: float
    age_s: float


class Geofence:
    """Avoid GPS jitter by requiring multiple confirmed outside/inside fixes.

    'outside' is confirmed only if the *nearest plausible distance*
    is still beyond the radius plus the configured hysteresis margin.

    WARNING: Statistical uncertainty depends on the receiver's meaning of
    'accuracy_m'; GPS error is not a hard guarantee.
    """

    def __init__(self, radius_feet: float, confirmation_count: int = 2):
        if not isfinite(radius_feet) or not 50 <= radius_feet <= 10000:
            raise ValueError("radius_feet must be between 50 and 10000")
        if not 2 <= confirmation_count <= 10:
            raise ValueError("confirmation_count must be 2 to 10")
        self.radius_m = radius_feet * FEET_TO_METERS
        self.hysteresis_m = max(5.0, self.radius_m * 0.10)
        self.max_accuracy_m = min(20.0, max(10.0, self.radius_m * 0.30))
        self.count = confirmation_count
        self.status = "unknown"
        self.outside_streak = 0
        self.inside_streak = 0

    def ingest(self, sample: Sample) -> dict:
        for value in (sample.distance_m, sample.accuracy_m, sample.age_s):
            if not isfinite(value) or value < 0:
                raise ValueError("all sample values must be nonnegative finite numbers")
        if sample.age_s > 45:
            self.outside_streak = 0
            self.inside_streak = 0
            return {"status": self.status, "measurement": "stale", "alert": None}
        if sample.accuracy_m > self.max_accuracy_m:
            self.outside_streak = 0
            self.inside_streak = 0
            return {"status": self.status, "measurement": "unreliable", "alert": None}

        if sample.distance_m - sample.accuracy_m > self.radius_m + self.hysteresis_m:
            side = "outside"
        elif sample.distance_m + sample.accuracy_m < self.radius_m - self.hysteresis_m:
            side = "inside"
        else:
            side = "uncertain"

        alert = None
        if side == "outside":
            self.outside_streak += 1
            self.inside_streak = 0
            if self.outside_streak >= self.count and self.status != "outside":
                self.status = "outside"
                alert = "zone_exit"
        elif side == "inside":
            self.inside_streak += 1
            self.outside_streak = 0
            if self.inside_streak >= self.count and self.status != "inside":
                self.status = "inside"
                if self.status != "unknown":
                    alert = None  # do not send nonessential reentry push
        else:
            self.inside_streak = 0
            self.outside_streak = 0
        return {"status": self.status, "measurement": side, "alert": alert}


def connection_warning(seconds_since_last_received: float) -> bool:
    """Independent signal-loss alarm; should run server-side on a schedule."""
    if not isfinite(seconds_since_last_received) or seconds_since_last_received < 0:
        raise ValueError("seconds_since_last_received must be nonnegative and finite")
    return seconds_since_last_received >= 90
