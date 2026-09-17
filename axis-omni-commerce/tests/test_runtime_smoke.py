from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from agents.registry import AgentRegistry
from database.models import AxisOmniDB
from orchestrator.engine import AxisOmniEngine
from policy.engine import PolicyEngine


class RuntimeSmokeTest(unittest.TestCase):
    def test_run_starts_and_routes(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = AxisOmniDB(Path(tmp) / "test.db")
            engine = AxisOmniEngine(AgentRegistry(ROOT), db, PolicyEngine())
            state = engine.start("smoke test")
            engine.route(state, "AXIS", "SUPPLIER_CATALOG_INTAKE")
            self.assertEqual(state.current_role, "AXIS")
            self.assertEqual(state.stage, "SUPPLIER_CATALOG_INTAKE")

    def test_verity_blocks_unauthorized_product(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = AxisOmniDB(Path(tmp) / "test.db")
            engine = AxisOmniEngine(AgentRegistry(ROOT), db, PolicyEngine())
            state = engine.start("gate test")
            engine.verity_gate(state, {
                "supplier_verified": True,
                "resale_authorized": False,
                "returns_defined": True,
                "tracking_supported": True,
                "platform_permitted": True,
                "contribution_margin_percent": 40,
            })
            self.assertEqual(state.status.value, "BLOCKED")

    def test_live_publish_requires_approval(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = AxisOmniDB(Path(tmp) / "test.db")
            engine = AxisOmniEngine(AgentRegistry(ROOT), db, PolicyEngine())
            state = engine.start("approval test")
            engine.request_action(state, "publish_live_product")
            self.assertEqual(state.status.value, "WAITING_APPROVAL")


if __name__ == "__main__":
    unittest.main()
