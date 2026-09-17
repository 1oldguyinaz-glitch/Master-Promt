from __future__ import annotations

from typing import Any, Iterable

from .base import CommerceConnector


class ShopifyAdapter(CommerceConnector):
    """Boundary for Shopify integration.

    The ChatGPT Shopify connector is currently the authorized execution surface.
    This class intentionally contains no embedded credentials. Replace method
    bodies with official authenticated API calls only after production access is
    explicitly configured. Until then, all write methods remain draft-only or
    raise to prevent accidental live commerce actions.
    """

    def __init__(self, store_domain: str, draft_only: bool = True) -> None:
        self.store_domain = store_domain
        self.draft_only = draft_only

    def healthcheck(self) -> dict[str, Any]:
        return {"platform": "shopify", "store_domain": self.store_domain,
                "draft_only": self.draft_only, "status": "CONFIGURED_NOT_AUTHENTICATED_IN_CODE"}

    def list_catalog(self) -> Iterable[dict[str, Any]]:
        return []

    def get_inventory(self, sku: str) -> dict[str, Any]:
        return {"sku": sku, "status": "UNKNOWN", "source": "shopify_adapter_stub"}

    def create_draft_listing(self, product: dict[str, Any]) -> dict[str, Any]:
        return {"status": "READY_FOR_AUTHORIZED_SHOPIFY_TOOL",
                "mode": "DRAFT", "product": product}

    def submit_order(self, order: dict[str, Any]) -> dict[str, Any]:
        raise PermissionError("Order submission disabled until supplier and live-commerce approval gates pass")

    def get_tracking(self, external_order_id: str) -> dict[str, Any]:
        return {"external_order_id": external_order_id, "tracking": None,
                "status": "NOT_CONNECTED"}
