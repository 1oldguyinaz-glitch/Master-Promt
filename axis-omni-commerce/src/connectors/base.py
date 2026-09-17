from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable


class CommerceConnector(ABC):
    """Contract all platform/supplier connectors must satisfy."""

    @abstractmethod
    def healthcheck(self) -> dict[str, Any]: ...

    @abstractmethod
    def list_catalog(self) -> Iterable[dict[str, Any]]: ...

    @abstractmethod
    def get_inventory(self, sku: str) -> dict[str, Any]: ...

    @abstractmethod
    def create_draft_listing(self, product: dict[str, Any]) -> dict[str, Any]: ...

    @abstractmethod
    def submit_order(self, order: dict[str, Any]) -> dict[str, Any]: ...

    @abstractmethod
    def get_tracking(self, external_order_id: str) -> dict[str, Any]: ...
