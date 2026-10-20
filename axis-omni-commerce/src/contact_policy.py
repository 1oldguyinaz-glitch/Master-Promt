"""AXIS shared, read-only cross-channel contact preflight.

This is a reference policy gate, NOT a live sending integration. All connectors
must run this gate and their own current provider/legal preflight before sends.
Never use business-name similarity as proof of a cross-platform identity.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

CHANNELS = frozenset({"email", "sms", "voice", "facebook", "instagram", "linkedin", "whatsapp"})
GLOBAL_NO_CONTACT = frozenset({"ACTIVE_NO_CONTACT", "ACTIVE_NO_AUTO_CONTACT"})
EMAIL_FAILURES = frozenset({"HARD_BOUNCE", "DNS_FAILURE"})


@dataclass(frozen=True)
class ContactDecision:
    permitted_for_provider_review: bool
    reason: str
    suppression_id: str = ""


def read_suppressions(path: str | Path) -> list[dict[str, str]]:
    """Read the existing AXIS suppression CSV without changing its format."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _norm(value: object, kind: str) -> str:
    value = str(value or "").strip().lower()
    if kind == "phone":
        digits = "".join(ch for ch in value if ch.isdigit())
        if len(digits) == 10:
            digits = "1" + digits
        return digits
    if kind in ("facebook", "instagram", "linkedin", "whatsapp"):
        return value.rstrip("/")
    return value


def _values(lead: Mapping, kind: str) -> set[str]:
    raw = lead.get("identities", {}).get(kind, [])
    if isinstance(raw, str):
        raw = [raw]
    return {_norm(value, "phone" if kind in ("phone", "sms", "voice") else kind)
            for value in raw if str(value).strip()}


def _matches(row: Mapping[str, str], lead: Mapping) -> bool:
    kind = row.get("scope", "").strip().lower()
    value = row.get("value", "")
    if not value:
        return False
    if kind in ("business", "business_id"):
        return _norm(value, kind) == _norm(lead.get("business_id"), kind)
    if kind == "phone":
        return _norm(value, kind) in _values(lead, "phone")
    if kind == "email":
        return _norm(value, kind) in _values(lead, "email")
    if kind == "domain":
        # Only verified business-domain aliases; never assume Gmail/Yahoo
        # users at the same free-mail domain belong to one company.
        return _norm(value, kind) in _values(lead, "domain")
    if kind in ("facebook", "instagram", "linkedin", "whatsapp"):
        return _norm(value, kind) in _values(lead, kind)
    return False


def evaluate_outbound(
    lead: Mapping,
    channel: str,
    suppressions: Sequence[Mapping[str, str]],
    *,
    owner_approved: bool = False,
    provider_permission_verified: bool = False,
) -> ContactDecision:
    """Fail-closed first-stage check; True never sends or authorizes a send.

    A verified identity link means explicit corroboration of the SAME business,
    not matching names or assumed social accounts. A provider-specific workflow
    must separately verify consent, messaging window, sender registration, and
    applicable rules. Owner approval and current provider eligibility required.
    """
    channel = channel.strip().lower()
    if channel not in CHANNELS:
        return ContactDecision(False, "unsupported_channel")
    if not lead.get("business_id") or lead.get("identity_links_verified") is not True:
        return ContactDecision(False, "unverified_business_identity")
    if not owner_approved:
        return ContactDecision(False, "owner_approval_required")
    if not provider_permission_verified:
        return ContactDecision(False, "provider_permission_unverified")

    # Profile must have a verified channel identity, not merely an email.
    identity_kind = "phone" if channel in ("sms", "voice") else channel
    if not _values(lead, identity_kind):
        return ContactDecision(False, "channel_identity_missing")

    # Evaluate suppressions over ALL verified identifiers for the same business.
    # An email STOP then prevents switching to SMS, Messenger, or LinkedIn.
    for row in suppressions:
        if not _matches(row, lead):
            continue
        status = row.get("status", "").upper().strip()
        reason = row.get("reason", "").upper().strip()
        suppression_id = row.get("suppression_id", "")
        if status in GLOBAL_NO_CONTACT or reason.startswith("OPT_OUT") or reason == "OWNER_EXCLUSION":
            return ContactDecision(False, "business_or_contact_dnc", suppression_id)
        if status == "ACTIVE_NO_RETRY" and (
            (row.get("scope", "").lower().strip() in ("email", "domain") and channel == "email")
            or (row.get("scope", "").lower().strip() == "phone" and channel in ("sms", "voice"))
        ):
            return ContactDecision(False, "channel_delivery_failure", suppression_id)

    return ContactDecision(True, "requires_final_provider_and_consent_preflight")
