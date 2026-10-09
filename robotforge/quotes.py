"""Optimize a supplied *verified* quote table. No live prices or scraping."""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from itertools import product
from math import prod


@dataclass(frozen=True)
class Offer:
    category: str
    part_number: str
    supplier: str
    unit_price: Decimal
    shipping_cost: Decimal
    url: str
    compatible: bool = True
    in_stock: bool = True


def _money(number: object) -> Decimal:
    try:
        value = Decimal(str(number))
    except (InvalidOperation, TypeError):
        raise ValueError("invalid price")
    if not value.is_finite() or value < 0:
        raise ValueError("price must be nonnegative and finite")
    return value


def compare_quotes(required_categories: list[str], supplier_quotes: list[dict]) -> dict:
    """Find minimum equipment + one freight charge per supplier (pre-tax).

    All offers must include category, part_number, supplier, unit_price,
    shipping_cost, url, compatible, and in_stock. Vendor shipping must be a
    consistent per-order charge across that vendor's quotes; otherwise a
    checkout-specific shipping calculation is required.
    """
    if not required_categories or len(required_categories) > 12:
        raise ValueError("require between 1 and 12 unique categories")
    if len(set(required_categories)) != len(required_categories):
        raise ValueError("categories must be unique")
    if not supplier_quotes or len(supplier_quotes) > 200:
        raise ValueError("require between 1 and 200 supplier quotes")
    offers = []
    all_shipping = {}
    for raw in supplier_quotes:
        required = {"category", "part_number", "supplier", "unit_price", "shipping_cost", "url", "compatible", "in_stock"}
        if not isinstance(raw, dict) or not required.issubset(raw):
            raise ValueError("each quote must include all required fields")
        offer = Offer(
            category=str(raw["category"]),
            part_number=str(raw["part_number"]),
            supplier=str(raw["supplier"]),
            unit_price=_money(raw["unit_price"]),
            shipping_cost=_money(raw["shipping_cost"]),
            url=str(raw["url"]),
            compatible=raw["compatible"] is True,
            in_stock=raw["in_stock"] is True,
        )
        if not offer.url.startswith("https://") or not offer.supplier or not offer.part_number:
            raise ValueError("quote requires HTTPS product link, supplier, and part number")
        if offer.supplier in all_shipping and all_shipping[offer.supplier] != offer.shipping_cost:
            raise ValueError("supplier shipping varies by item; request checkout-level shipping quote")
        all_shipping[offer.supplier] = offer.shipping_cost
        if offer.compatible and offer.in_stock:
            offers.append(offer)
    options = [[o for o in offers if o.category == category] for category in required_categories]
    missing = [category for category, choices in zip(required_categories, options) if not choices]
    if missing:
        return {"status": "missing_offers", "missing_categories": missing}
    if prod(len(group) for group in options) > 100000:
        raise ValueError("too many combinations; narrow quotes")
    winner = None
    for combination in product(*options):
        suppliers = {o.supplier for o in combination}
        parts = sum((o.unit_price for o in combination), Decimal(0))
        freight = sum((all_shipping[name] for name in suppliers), Decimal(0))
        total = parts + freight
        if winner is None or total < winner[0]:
            winner = (total, parts, freight, combination)
    total, parts, freight, combination = winner
    return {
        "status": "quote_based_estimate",
        "currency": "USD",
        "parts": str(parts),
        "shipping": str(freight),
        "total_pre_tax": str(total),
        "excluded": ["tax", "service plan", "tools", "unlisted accessories"],
        "quote_validation": "Supplied quotes were not independently verified.",
        "items": [
            {"category": o.category, "part_number": o.part_number,
             "supplier": o.supplier, "unit_price": str(o.unit_price), "url": o.url}
            for o in combination
        ],
    }
