"""RobotForge read-only hardware-design MCP plugin prototype.

Run with: pip install -r requirements.txt && python server.py
No live telemetry, guardian accounts, push notifications, or supplier APIs here.
"""
from mcp.server.fastmcp import FastMCP
from geofence import Geofence, Sample, connection_warning
from quotes import compare_quotes

mcp = FastMCP("RobotForge", stateless_http=True, json_response=True)


@mcp.tool()
def design_child_tracker(radius_feet: float = 300) -> dict:
    """Draft a safe-zone child wearable reference design; no live location access.

    radius_feet is adjustable from 50 to 10,000 feet. Accuracy and latency
    constraints mean tiny zones cannot be promised to work instantaneously.
    """
    g = Geofence(radius_feet)
    return {
        "name": "Child geofence wearable",
        "status": "reference prototype, not deployable safety equipment",
        "configurable_radius_feet": radius_feet,
        "initial_anchor": "saved fixed place; moving-parent mode deferred",
        "reference_parts": [
            "Circuit Dojo nRF9151 Feather, LTE-M and GNSS development board",
            "manufacturer-compatible LTE/GNSS antennas",
            "carrier-verified LTE-M SIM and service",
            "protected rechargeable battery and appropriate charge circuitry",
            "professionally tested, enclosed clip-on housing"
        ],
        "architecture": [
            "device acquires location and reports securely to private backend",
            "backend stores minimal authorized location history",
            "server checks uncertainty-aware geofence and missing-report alarm",
            "authenticated guardian app receives push and displays dated last fix"
        ],
        "algorithm": {
            "exit_confirmations": g.count,
            "accuracy_limit_m": round(g.max_accuracy_m, 2),
            "hysteresis_m": round(g.hysteresis_m, 2),
            "stale_fix_after_s": 45,
            "missing_report_alarm_s": 90
        },
        "limitations": [
            "GPS/indoor blockage, position errors, and cellular gaps",
            "GPS and LTE can require separate duty cycles on some modems",
            "notification delivery can be delayed",
            "bench development board must not be worn by a child",
            "real prices, stock, tax, shipping, data fees not sourced by this tool"
        ],
        "test_plan": [
            "bench simulation",
            "outdoor adult-carried accuracy measurements",
            "no-signal/low-battery drill",
            "independent caregiver review and child-safety engineering"
        ]
    }


@mcp.tool()
def simulate_geofence(radius_feet: float, synthetic_samples: list[dict]) -> dict:
    """Test exit logic with SYNTHETIC distance_m, accuracy_m, age_s only.

    Never provide a child's live GPS coordinates or identity to this tool.
    """
    if len(synthetic_samples) > 200:
        raise ValueError("maximum 200 synthetic samples")
    engine = Geofence(radius_feet)
    events = []
    for sample in synthetic_samples:
        result = engine.ingest(Sample(
            float(sample["distance_m"]),
            float(sample["accuracy_m"]),
            float(sample["age_s"])))
        events.append(result)
    return {"events": events, "final_status": engine.status}


@mcp.tool()
def compare_part_quotes(required_categories: list[str], supplier_quotes: list[dict]) -> dict:
    """Optimize manual verified supplier offers; this does NOT search live stores.

    Compare all required parts including one fixed per-supplier shipping fee.
    Every quote must specify HTTPS URL, availability, and compatibility.
    """
    return compare_quotes(required_categories, supplier_quotes)


@mcp.tool()
def test_connection_warning(seconds_since_last_report: float) -> bool:
    """Test synthetic loss-of-signal alarm; not a live background monitor."""
    return connection_warning(seconds_since_last_report)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
