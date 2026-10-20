# AXIS Omni — One business / multichannel identity / shared DNC (v0.1)

Status: **reference policy gate added; no live SMS, social, or voice integrations enabled.**

## Objective

A lead is one canonical **business_id**, not a collection of unrelated messages.
Preserve one contact/conversation history across Gmail, SMS, phone, Facebook
Messenger, Instagram, LinkedIn, and WhatsApp when official integrations permit it.

Multiple usable channels **do not** justify simultaneous automated solicitation.
Choose the contextually appropriate, authorized contact path, and coordinate
future actions against the same CRM record.

## Canonical business record (illustrative — not an imported lead)

\`\`\`json
{
  "business_id": "axis-company-001",
  "business_name": "Example Plumbing",
  "identity_links_verified": true,
  "identity_evidence": [
    {"source": "business website", "url": "https://example-plumbing.test/contact", "checked_at": "2026-10-19"}
  ],
  "identities": {
    "email": ["office@example-plumbing.test"],
    "domain": ["example-plumbing.test"],
    "phone": ["+12535550136"],
    "facebook": ["123456789"],
    "instagram": [],
    "linkedin": ["https://www.linkedin.com/company/example-plumbing/"],
    "whatsapp": []
  },
  "channel_permissions": {
    "email": "owner_and_sender_review_required",
    "sms": "explicit_marketing_consent_and_registration_required",
    "voice": "applicable_telemarketing_rules_and_internal_approval_required",
    "facebook": "approved_page_api_and_permitted_message_context_required",
    "instagram": "approved_professional_account_api_and_permitted_thread_required",
    "linkedin": "approved_api_product_and_permitted_message_context_required",
    "whatsapp": "opt_in_and_approved_business_message_rules_required"
  },
  "conversation_events": [],
  "lifecycle": "sourced"
}
\`\`\`

The identity is verified ONLY when an authorized source corroborates the connection.
A shared business name, a Google/Gmail/Yahoo domain, location similarity, or an
unverified social page is not proof of identity. Disputed matches go to owner
review, not automatic merge.

## Shared DNC semantics

The existing \`outreach/suppressions.csv\` remains the source for legacy
suppression events and its format is unchanged. New, verified identifiers may
use \`scope\`: \`business_id\` (or \`business\`), \`email\`, \`domain\`,
\`phone\`, \`facebook\`, \`instagram\`, \`linkedin\`, or \`whatsapp\`.

- An explicit STOP, removal request, not-interested/refusal, or owner exclusion
  against ANY verified identity blocks promotional outreach across ALL channels
  for that canonical business/contact. Do not switch channels to bypass refusal.
- Delivery failures such as a hard email bounce or DNS error block retries on
  the failed email channel/identity. They do not alone establish a global
  refusal via phone/social.
- Future suppression records must include evidence, scope, event timestamp,
  reason, and status; owner-approved, evidenced overrides must be audited.
- Never automatically treat unrelated companies with the same name as one DNC
  identity; escalate ambiguous matches.
- Before EVERY outbound attempt, check current suppressions and channel
  permissions; cache invalidation and race-safe enforcement are required in
  production, with a fresh check immediately before dispatch.

## Reference preflight module

\`src/contact_policy.py\` implements a dependency-free, read-only policy check:

\`\`\`python
from contact_policy import read_suppressions, evaluate_outbound

rows = read_suppressions("outreach/suppressions.csv")
decision = evaluate_outbound(
    verified_lead,
    "sms",
    rows,
    owner_approved=True,
    provider_permission_verified=True,
)
if not decision.permitted_for_provider_review:
    # Do not dispatch; log reason and suppression ID.
    ...
else:
    # Still require live SMS consent, registration, opt-out and provider preflight.
    ...
\`\`\`

\`permitted_for_provider_review=True\` DOES NOT authorize sending. It only
indicates the profile passed the first gate. Live credentials, legal/consent
checks, transport restrictions, authorization, and logging remain separate.
No connector currently calls this module automatically.

## Implementation sequence

1. **Ingest and reconcile:** import the 700+ Gmail outreach candidates and
   existing repository phone leads; retain provenance, identity confidence,
   verified links, and message/bounce history. Do not assume each email lead
   has a phone number.
2. **Deduplicate:** owner-review uncertain links. Create stable business IDs
   and independent person records as needed; prevent shared-domain collision.
3. **Global DNC sync:** reconcile \`suppressions.csv\` with Gmail DNC labels;
   preserve all existing opt-outs, no-retry events, and exclusions.
4. **Authorized connectors:** Gmail first; SMS via a registered provider;
   official Meta Page/Instagram APIs with permissions and message windows;
   LinkedIn only via approved API products; WhatsApp via Business Platform.
   Do not scrape, impersonate, or automate prohibited DMs.
5. **Conversation orchestration:** contact events -> Sentinel -> STAN
   qualification -> VERITY approval check -> owner-approved action -> CRM
   history and BEACON metrics. Owner remains the sales sender/closer.
6. **Acceptance gate:** test identity matching, STOP propagation, compliance,
   provider rejection, idempotency, message windows, and audit logs using
   sandbox accounts before any live sending.

## Commercial direction

Axis is a high-ticket managed business system with separate monthly support.
Multichannel orchestration serves discovery, qualification, meetings, and
measured results — not contact volume for its own sake.

**No paid campaigns, outbound texts, social DMs, or voice calls have been
authorized by this document.**
