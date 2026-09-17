from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PolicyDecision:
    allowed: bool
    approval_required: bool = False
    reason: str = ""


class PolicyEngine:
    """Deterministic gates. Money and permissions are never delegated to model judgment."""

    def __init__(self, minimum_margin_percent: float = 20.0) -> None:
        self.minimum_margin_percent = minimum_margin_percent

    def check_product(self, product: dict[str, Any]) -> PolicyDecision:
        required = [
            "supplier_verified",
            "resale_authorized",
            "returns_defined",
            "tracking_supported",
            "platform_permitted",
        ]
        missing = [k for k in required if not product.get(k)]
        if missing:
            return PolicyDecision(False, False, f"Eligibility gate failed: {', '.join(missing)}")

        margin = product.get("contribution_margin_percent")
        if margin is None:
            return PolicyDecision(False, False, "Contribution margin is unknown")
        if float(margin) < self.minimum_margin_percent:
            return PolicyDecision(False, False, "Contribution margin below policy minimum")

        return PolicyDecision(True)

    def check_action(self, action: str, amount: float = 0.0) -> PolicyDecision:
        always_human = {
            "publish_live_product",
            "sign_supplier_contract",
            "connect_financial_account",
            "purchase_inventory",
            "enable_ad_spend",
            "share_sensitive_customer_data",
            "irreversible_delete",
        }
        if action in always_human:
            return PolicyDecision(False, True, f"Human approval required for {action}")
        if amount > 0:
            return PolicyDecision(False, True, "Any spend requires approval in draft-only mode")
        return PolicyDecision(True)
