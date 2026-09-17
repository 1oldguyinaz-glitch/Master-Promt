from pathlib import Path

from agents.registry import AgentRegistry
from database.models import AxisOmniDB
from intelligence.signals import HistoricalSignalStore
from orchestrator.engine import AxisOmniEngine
from policy.engine import PolicyEngine


def build_engine(repo_root: Path | None = None) -> tuple[AxisOmniEngine, AxisOmniDB, Path]:
    root = repo_root or Path(__file__).resolve().parents[1]
    db = AxisOmniDB(root / "axis_omni.db")
    registry = AgentRegistry(root)
    policy = PolicyEngine(minimum_margin_percent=20.0)
    engine = AxisOmniEngine(registry=registry, db=db, policy=policy)
    return engine, db, root


if __name__ == "__main__":
    engine, db, root = build_engine()
    signal_store = HistoricalSignalStore(db)
    signals = signal_store.load_json(root / "data" / "beacon_seed_signals_v1.json")

    state = engine.start("Prove one supplier-catalog-to-Shopify-draft workflow")
    state.record("historical_signals_loaded", count=len(signals))
    engine.route(state, "AXIS", "SUPPLIER_CATALOG_INTAKE")
    print(state.to_json())
