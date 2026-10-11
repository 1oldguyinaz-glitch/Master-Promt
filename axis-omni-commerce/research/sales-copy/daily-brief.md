# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-11 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis Washington Business Hours / Axis 450 Outreach, with Sentinel validation and BEACON measurement.

## Decision

Preserve the approved controls and ordered test sequence. **CL-004 remains the only active copy test.** CL-005 and CL-008 remain queued, not concurrent; CL-006 and CL-007 remain backlog. Do not change copy/winners.json.

No copy winner is promoted. The operational ceiling remains **450 confirmed prospect-facing sends per Pacific day**, but it never overrides DNC, eligibility, provider capacity, test isolation, compliance or list quality.

Add one operational guardrail, not a copy winner: preserve plain-text first touches without open-tracking pixels or attachments. Keep the single visible booking link secondary to the reply question. If tracking infrastructure changes, log it as a separate treatment; do not compare the resulting cohorts as if only copy changed.

## Axis evidence observed

Sources: durable lead ledger blob `56273891d016373c2275a37946c708db59b86b66`; October 11 run reports at blobs `67cd0d7a98ae7be908f32eb8246ba2ceef66b863` and `83c981029c8e002565c2a5ca04cfe6c9c688c208`; paginated Axis Gmail Sent reconciliation.

- Verified CL-004 accepted-send window: October 8 **21**, October 9 **10**, October 10 **0**, and October 11 through 07:55 Pacific **7** prospect-facing sends; current accepted exposure **n=38**.
- Raw Gmail Sent contained additional non-prospect/internal messages on October 8–9; those were not counted as CL-004 exposures.
- Reported outcomes in this window: **0 positive replies, 0 qualified conversations, 0 confirmed bookings, $0 supported revenue, 2 clear opt-outs and 2 verified delivery failures**.
- October 11 inbox review found no new replies, bounces, opt-outs, bookings or payments. The live DNC label remained 5 messages across 3 threads.
- Delivery remains unknown for accepted messages without a verified delivery event. Response windows are immature; no lift, delivery rate or winner is claimed.

## Evidence review

| Area | Evidence reviewed | Assessment for Axis |
|---|---|---|
| Subject lines | Current vendor roundups mix open-rate studies, client cohorts and undocumented methods. Google states it does not track or verify third-party open rates. | No new subject winner. Keep CL-007 in backlog; opens remain diagnostic only. |
| Opening / problem framing | Snov.io reports higher replies for personalized campaigns (0.58% vs 0.42%) but also higher bounces (2.55% vs 1.29%) and unsubscribes (0.07% vs 0.03%). This is observational and likely confounded by list/source differences. | Preserve CL-001: one verifiable operational detail, no invented pain, praise or familiarity. No causal claim. |
| Outcome framing | No new randomized evidence isolates outcome language for local-business outreach. | Preserve the approved concise relevance bridge; do not import ROI claims or promise outcomes. |
| CTA | No new causal evidence improves on the queued CL-005 question-versus-value-offer comparison. | Keep one primary reply question and the booking link secondary. CL-005 remains queued. |
| Follow-up | Snov.io reports the same average reply rate (0.41%) for campaigns with and without follow-ups while total reply counts differ; public denominators and eligibility are not sufficient for a causal lift estimate. | CL-008 remains a randomized one-follow-up test among eligible nonresponders. Do not adopt multi-step vendor sequences. |
| AI-written tone | A 2026 randomized crossover field experiment covering 16,880 workplace emails found playful/professional GPT-5 rewrites changed emotional positivity but did not directly change opens, replies or response time. The population was internal workplace email, not cold outreach. | Do not add a playful-tone test or “AI-polished” winner. Preserve Bradley’s natural, factual voice. |
| Tracking / attachments | Snov.io observational data associates no link tracking with higher replies (0.87% vs 0.21%) and attachments with higher bounce (2.98% vs 1.86%). Treatment assignment and list comparability are not documented. | Strong enough only to preserve a low-risk operating guardrail: no open pixel and no first-touch attachment. Not strong enough to claim causal lift. |
| Deliverability | Google requires authentication, accurate headers and gradual sending; after a quota error it advises a pause, diagnosis and paced single-connection recovery. Google also advises spam below 0.1% and never 0.3% or higher. | Provider and reputation limits override the 450 ceiling. Reconcile Sent before any retry. |
| Compliance | FTC guidance says CAN-SPAM covers B2B commercial email and requires truthful headers/subjects, a valid postal address, a clear opt-out and prompt honoring of opt-outs. | Preserve verified sender identity/address and exact STOP instruction. DNC is hard no-send across all arms. |
| Benchmarks | Instantly and Snov.io publish useful practitioner ranges, but populations, denominators, delivery definitions and causal methods vary. | No external rate becomes an Axis target. Report exact Axis numerators, denominators and windows. |

No consequential AI-automation, booking-site, local-acquisition or TikTok development reviewed today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable sourced detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain text from Bradley with truthful identity, approved offer, complete private-config footer and exact opt-out.
- **Deliverability guardrail:** no open-tracking pixel and no first-touch attachment; any tracking change is an infrastructure treatment, not a copy-only comparison.

These are operating controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact versions. Hold sender, offer, eligibility, cadence, tracking and compliance constant except for the named variable. Deduplicate by business and recipient.

Primary outcome: positive replies within 14 days. Secondary outcomes: qualified conversations, confirmed bookings at 30 and 60 days, and supported revenue/contact at 60 and 90 days. Guardrails: opt-outs, complaints and verified failure classes. Track bookings independently of replies. Use delivered denominators only when delivery is verified; otherwise report accepted/Sent and label delivery unknown.

**Sample P:** after an Axis baseline exists, calculate per-version sample size for a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until then, 200–400 eligible recipients per version is only a feasibility pilot, never proof.

**Rule K:** keep only if the primary endpoint’s 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to bookings, revenue, opt-outs, complaints or failures. Retire when the interval rules out that effect. Otherwise label inconclusive. Safety stops override sample completion.

## Ordered hypotheses

| Order / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Approved AI/automation-led question | Sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Qualified conversations; 30/60-day bookings; 60/90-day revenue/contact | P; current accepted n=38, delivery incomplete | K; immediate kill for fabricated, stale or unsupported relevance; provider/DNC stops override |
| 2 / CL-005 | Discovery question | Offer to share two concrete observations; booking link secondary in both | Positive replies / eligible recipients | Qualified conversations, bookings, revenue/contact | P after CL-004 endpoint | K; reject if reply lift lacks downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized eligible nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop on any human reply, opt-out, bounce, complaint or DNC match |
| Backlog / CL-006 | Existing body length | 50–80 words, proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after prior endpoint | K; skip if control is already in range |
| Backlog / CL-007 | Existing truthful question subject | Truthful 1–4-word business-priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after prior endpoint | K; never select on opens alone |

## Executable handoff

1. Record this file’s date and verified blob SHA.
2. Reconcile paginated Axis Gmail Sent using the Pacific-day boundary, plus inbox, live DNC label, drafts, suppressions, failures, thread state and bookings.
3. Continue CL-004 only when the active sender workflow verifies DNC, suppression, daily count, eligible inventory and provider capacity. Do not force volume toward 450.
4. Do not start CL-005 concurrently. CL-008 is due only for randomized eligible nonresponders after five business days and after a fresh DNC/thread check.
5. Preserve plain text, no open pixel and no first-touch attachment. Keep the required booking link visible but secondary.
6. Keep every outbound message individually researched and distinct. A sourced observation may frame relevance; it may not assert an unobserved problem.
7. Use the private sender-address record at send time; never publish the address in this research file.
8. BEACON reports state × niche × arm × hypothesis with exact numerators, denominators, windows and reply classes. Unknown delivery remains unknown.
9. January/Infoton and every DNC/suppressed identity remain no-send.
10. No prospect email may be sent by COPY LAB.

## Copy-library decision

**No new copy finding qualifies as an approved winner.** Preserve the existing control library and test order.

Add only this operational guardrail:

- First touches remain plain text, without open-tracking pixels or attachments.
- The booking link remains a visible secondary path, not a tracked primary CTA.
- Open rate is diagnostic only; winner selection uses positive replies, bookings and revenue.
- External claims must retain population, period, numerator, denominator, reply definition and causal limitations.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 11, 2026

1. Axis Washington Outreach Run, October 11 06:57 Pacific: https://github.com/1oldguyinaz-glitch/Master-Promt/blob/main/axis-omni-commerce/outreach/runs/2026-10-11-0657-washington.md
2. Axis Washington Outreach Run, October 11 07:55 Pacific: https://github.com/1oldguyinaz-glitch/Master-Promt/blob/main/axis-omni-commerce/outreach/runs/2026-10-11-0755-washington.md
3. Axis durable lead ledger: https://github.com/1oldguyinaz-glitch/Master-Promt/blob/main/axis-omni-commerce/data/leads/2026-09-29-recovery-candidates-1829.csv
4. Google, “Email sender guidelines,” retrieved October 11, 2026: https://support.google.com/mail/answer/81126
5. FTC, “CAN-SPAM Act: A Compliance Guide for Business,” retrieved October 11, 2026: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
6. Snov.io, “Cold Email Statistics for 2026,” updated September 21, 2026: https://snov.io/blog/cold-email-statistics/
7. Instantly, “Cold Email Reply Rate Benchmarks (2026),” updated July 1, 2026: https://instantly.ai/blog/cold-email-reply-rate-benchmarks/
8. arXiv:2607.11749, randomized crossover field experiment on LLM-rewritten workplace email tone, retrieved October 11, 2026: https://arxiv.org/abs/2607.11749

Historical briefs and evidence remain in Git history. No prospect email was sent by COPY LAB.
