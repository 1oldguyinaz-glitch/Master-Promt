# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-02 (Pacific)
Status: RESEARCH AND VERIFIED REPOSITORY HANDOFF; ALL NEW TESTS UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision
Preserve the current control. **CL-004 remains the only planned copy test once outreach is legally and operationally eligible.** No campaign winner changes today. The daily ceiling remains 450 prospect-facing sends, including first touches, follow-ups and replies, subject to lower provider capacity.

## Axis evidence observed
- The latest persisted prospect-outreach checkpoint remains **0 confirmed prospect sends / 450**, zero positive prospect replies, zero qualified conversations and zero confirmed bookings/cancellations. No current Axis copy denominator exists.
- Four 2026-10-01 Sent messages were internal platform-safety reports, not prospect outreach. Later support replies were internal handoffs and do not count as prospect replies.
- The saved queue remains 15 candidates: 12 verified public business-email sources, two requiring source recheck and one quarantined; AZ 9 / WA 6 and sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- Gmail connectivity is verified, but no verified Axis physical postal address is persisted. New commercial outreach remains blocked. This is a compliance condition, not a copy-performance diagnosis.
- No experiment was deployed and no winner changed.

## Evidence review
### Verified or strong operational findings
1. **Compliance and deliverability outrank copy changes.** Google requires accurate identity, authentication, low complaint rates and monitoring. Its current guidance says to keep Postmaster spam rates below 0.10% and avoid 0.30% or higher. FTC guidance requires accurate headers and subject lines, a working opt-out and a valid physical postal address. These are guardrails, not conversion hypotheses. [1–4]
2. **Open rate remains diagnostic only.** Privacy and proxy loading can distort it. Axis selects on positive replies, booked meetings per delivered email and downstream revenue.
3. **Generic AI personalization has no demonstrated conversion advantage.** A 2026 benchmark built from 6,279 sales success stories found a personalization plateau and no statistically separating model on one Fortune 100 cohort. Its 12-representative field deployment measured immediate usefulness, not recipient replies, bookings or revenue. Treat it as evidence for human verification and sourced relevance—not as proof that personalization raises conversion. [5]
4. **Valid tool calls are not verified workflow completion.** EmailBench reports 99.7% tool-call completion for its best configuration but only 33.5% scenario completion. It uses synthetic enterprise-email tasks rather than sales outreach, so it changes no copy rule; it reinforces the existing requirement to verify Gmail IDs, persistence, suppression and outcomes independently. [6]

### Useful but weak claims
- Vendor datasets still associate concise bodies, relevant openings, small segmented lists and follow-ups with higher replies. These are observational and confounded by list quality, offer, industry and infrastructure. They generate hypotheses, not Axis forecasts. [7–10]
- A newly surfaced 2M+ cold-email report states a 2.09% overall reply rate, 14.1% positive share of replies and a 0.64% interested-reply rate. Those published figures are arithmetically inconsistent: 2.09% × 14.1% is approximately 0.29%, not 0.64%. Do not add its headline benchmark to the Axis copy library without raw-method clarification. [7]
- The 2026 randomized workplace-email study still found no direct open, reply or response-time lift from playful versus professional AI rewriting. It was not cold local-business outreach, so tone-only rewriting remains deprioritized rather than disproven. [11]
- Claims of large lifts from first-name tokens, personalized subjects or hyper-personalized AI copy remain weak without transparent randomized recipient-level evidence and downstream metrics.

## Controls and hypotheses
Preserve CL-001 sourced situational relevance, CL-002 one discovery CTA plus secondary booking link, and CL-003 concise copy as controls—not proven winners. CL-004 through CL-008 remain unproven. Defer CL-005 through CL-008 until CL-004 reaches its preregistered endpoint.

Common design: randomize by business; stratify by state, niche and sticky arm; freeze exact versions; keep eligibility, offer, pricing, sender, cadence and compliance identical; deduplicate businesses. Primary windows: 14 days positive replies, 30 days bookings, 60 days revenue. Autoreplies, opt-outs and negative replies are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent.

**Sample P:** calculate from the observed Axis baseline and a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until a baseline exists, 200–400 per version is only a feasibility pilot.
**Rule K:** keep only when the endpoint 95% interval excludes zero and reaches the worthwhile effect without material harm to bookings/revenue, opt-outs, complaints or bounces. Retire when the interval rules out the worthwhile effect; otherwise mark inconclusive. Safety stops override sample completion.

| ID | Control | Variant / hypothesis | Primary metric | Secondary metric | Sample requirement | Kill / keep rule |
|---|---|---|---|---|---|---|
| CL-004 | Existing AI/automation-led opening | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings, qualified conversations, revenue/contact, opt-outs | P | K; kill immediately for fabricated or unsupported relevance |
| CL-005 | Existing discovery question | Offer to share two useful observations; booking link secondary in both | Positive replies / recipients | Bookings, qualified conversations, revenue/contact | P after CL-004 | K; reject if reply lift does not improve downstream quality |
| CL-006 | Existing body length | 50–80 words; proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after CL-004 | K; skip if control is already in range |
| CL-007 | Existing truthful subject | Truthful 1–4-word priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after CL-004 | K; never select on opens alone |
| CL-008 | No follow-up | One useful follow-up after five business days to eligible randomized nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from nonresponder baseline | K; stop on any reply, opt-out, bounce or complaint |

## Executable handoff
1. Do not send until a verified current Axis street address, registered P.O. box or registered private mailbox is persisted in sender configuration and the footer. Never infer Bradley's home address.
2. Record this file's date and SHA. Reconcile paginated Gmail Sent with durable history; check inbox, suppressions, drafts, thread state and failure quarantines.
3. Use the existing control outside CL-004. First touch: Bradley identity, one sourced relevance point, possible outcome without promises, one primary question, secondary booking link and exact opt-out.
4. For CL-004 only, randomize eligible first-touch businesses within state × niche × sticky arm. Persist assignment, exact copy version, Gmail ID and accepted/delivery state.
5. Follow up only when due under an approved sequence or CL-008 assignment. Add useful information rather than repeating pressure. Stop on any human reply, opt-out, bounce or complaint.
6. Objections: opt-out/not interested → suppress without rebuttal; timing → acknowledge and obtain permission for a later date; price → use verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
7. Process sequential batches of 15–25, rechecking count, suppression and provider responses between batches. Never exceed 450 and never force volume through weak leads or provider limits.
8. BEACON reports state × niche × arm × hypothesis with numerators, denominators and intervals. Positive replies, bookings and revenue outrank opens. Unknown delivery remains unknown.

## Copy-library decision
**No new finding is strong enough to add as an approved winner.** Preserve the existing candidate pattern only: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Add no benchmark promise, generic first-name token rule, deceptive urgency, fake familiarity or autonomous-AI claim.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

Do not modify `copy/winners.json` without measured Axis evidence.

## Sources checked October 2, 2026
[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414
[3] FTC, CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
[4] FTC, registered P.O. boxes/private mailboxes: https://www.ftc.gov/news-events/news/press-releases/2008/05/ftc-approves-new-rule-provision-under-can-spam-act
[5] Srivastava et al., Benchmarking the Personalization Capabilities of Large Language Models (2026): https://arxiv.org/abs/2607.20471
[6] Singh et al., EmailBench (2026): https://arxiv.org/abs/2609.31906
[7] Sales.co, 2M+ cold-email report: https://sales.co/research/cold-email-statistics
[8] Saleshandy, 53.1M-email 2026 benchmark: https://www.saleshandy.com/blog/cold-email-statistics/
[9] Instantly, 2026 reply-rate benchmark: https://instantly.ai/blog/cold-email-reply-rate-benchmarks/
[10] Gong, executive cold-email analysis: https://dev.www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says
[11] Ben-Zion & Lazebnik, Playful AI in Professional Email (2026): https://arxiv.org/abs/2607.11749

Historical controls and prior evidence remain in Git history. Latest persisted outcomes read: `2026-10-01-0832-handoff.md`, `2026-10-01-1129-internal-handoff.md`, `2026-10-01-1232-uber-routing-correction.md`, and `2026-10-01-1526-doordash-handoff.md`.
