from pathlib import Path

from agents.registry import AgentRegistry
from database.models import AxisOmniDB
from orchestrator.engine import AxisOmniEngine
from policy.engine import PolicyEngine


def build_engine(repo_root: Path | None = None) -> AxisOmniEngine:
    root = repo_root or Path(__file__).resolve().parents[1]
    db = AxisOmniDB(root / "axis_omni.db")
    registry = AgentRegistry(root)
    policy = PolicyEngine(minimum_margin_percent=20.0)
    return AxisOmniEngine(registry=registry, db=db, policy=policy)


if __name__ == "__main__":
    engine = build_engine()
    state = engine.start("Prove one supplier-catalog-to-Shopify-draft workflow")
    engine.route(state, "AXIS", "SUPPLIER_CATALOG_INTAKE")
    print(state.to_json())
