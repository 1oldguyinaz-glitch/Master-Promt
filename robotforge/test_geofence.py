import unittest
from geofence import Geofence, Sample, connection_warning


class GeofenceTests(unittest.TestCase):
    def test_initial_inside_and_two_confirmed_exits(self):
        g = Geofence(radius_feet=300)
        for _ in range(2):
            g.ingest(Sample(distance_m=10, accuracy_m=4, age_s=2))
        self.assertEqual(g.status, "inside")
        self.assertIsNone(g.ingest(Sample(distance_m=150, accuracy_m=5, age_s=2))["alert"])
        self.assertEqual(g.ingest(Sample(distance_m=150, accuracy_m=5, age_s=2))["alert"], "zone_exit")

    def test_single_jump_does_not_trigger(self):
        g = Geofence(300)
        g.ingest(Sample(150, 5, 1))
        self.assertNotEqual(g.ingest(Sample(90, 10, 1))["alert"], "zone_exit")

    def test_accuracy_band_prevents_false_alarm(self):
        g = Geofence(300)
        for _ in range(4):
            response = g.ingest(Sample(98, 16, 1))
        self.assertIsNone(response["alert"])

    def test_stale_and_unreliable_fixes_rejected(self):
        g = Geofence(300)
        self.assertEqual(g.ingest(Sample(150, 5, 60))["measurement"], "stale")
        self.assertEqual(g.ingest(Sample(150, 40, 1))["measurement"], "unreliable")
        self.assertIsNone(g.ingest(Sample(150, 5, 1))["alert"])

    def test_anti_spam_when_already_outside(self):
        g = Geofence(300)
        alerts = [g.ingest(Sample(150, 5, 1))["alert"] for _ in range(5)]
        self.assertEqual(alerts.count("zone_exit"), 1)

    def test_connection_loss(self):
        self.assertFalse(connection_warning(89))
        self.assertTrue(connection_warning(90))

    def test_radius_validation(self):
        with self.assertRaises(ValueError):
            Geofence(0)

    def test_negative_accuracy_rejected(self):
        with self.assertRaises(ValueError):
            Geofence(300).ingest(Sample(100, -1, 1))


if __name__ == "__main__":
    unittest.main()
