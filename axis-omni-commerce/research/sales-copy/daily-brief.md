# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-03 (Pacific)
Status: RESEARCH AND VERIFIED REPOSITORY HANDOFF; ALL NEW TESTS UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision
Preserve the current control. **CL-004 remains the only planned copy test once outreach is legally and operationally eligible.** No campaign winner changes today. The daily ceiling remains 450 prospect-facing sends, including first touches, follow-ups and replies, subject to lower provider capacity.

## Axis evidence observed
- The latest persisted outreach checkpoint, `axis-omni-commerce/outreach/runs/2026-10-02-0833-handoff.md`, reports **0 confirmed prospect sends / 450**, zero positive prospect replies, zero qualified conversations and zero confirmed bookings/cancellations. Exact paginated Sent count was zero for the October 2 Pacific day.
- The saved queue remained 15 candidates: 12 verified public business-email sources, two requiring source recheck and one quarantined; AZ 9 / WA 6 and sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- The active hypothesis was CL-004, but exposure was zero. There is therefore no Axis copy denominator and no basis for declaring a winner.
- Gmail connectivity was verified, but no verified Axis physical postal address was persisted. New commercial outreach remained blocked. This is a compliance condition, not a copy-performance diagnosis.
- No experiment was deployed and no winner changed.

## Evidence review
### Verified or strong operational findings
1. **Compliance and deliverability outrank copy changes.** Google requires authentication, accurate sender identity, valid DNS, TLS and complaint control; for bulk senders it also requires DMARC alignment and one-click unsubscribe. FTC guidance applies to B2B commercial email and requires accurate headers and subject lines, ad identification, a valid physical postal address, a clear opt-out and honoring opt-outs within 10 business days. These are operating guardrails, not conversion hypotheses. [1–3]
2. **Open rate remains diagnostic only.** Proxy loading and privacy protection can distort it. Axis selects on positive replies, booked meetings per delivered email and downstream revenue.
3. **Tone-only rewriting has no demonstrated cold-outreach advantage.** A randomized crossover field experiment covering 16,880 workplace emails found playful versus professional GPT-5 rewriting changed tone but did not directly improve opens, replies or response time. The setting was internal workplace communication, not cold local-business outreach, so this deprioritizes tone-only testing rather than disproving it. [4]
4. **Large vendor datasets can suggest tests but cannot establish causal copy rules.** Gong describes analyses of 25 million cold emails and more than one million executive sales cycles; Lavender reports 231,818 cold emails. Neither public summary establishes randomized recipient-level causality for Axis outcomes. [5–6]

### Useful but weak claims
- Vendor studies commonly associate concise copy, specific relevance, one low-friction CTA, smaller segmented campaigns and useful follow-ups with higher replies. List quality, offer, sender reputation, industry and infrastructure are uncontrolled or incompletely reported. Treat these as hypothesis generators only.
- Saleshandy's 2026 page says its report covers 53.1 million cold emails and 60,000 sequences, but the same page claims 67.4 million connected email accounts. It also presents a 3.7% average reply rate alongside a 3–5% average positive-reply range. Those public figures are internally difficult to reconcile, so Axis must not adopt its headline lifts or benchmarks as library facts. [7]
- Claims that a particular subject length, first-name token, “quick question,” personalization depth or follow-up count reliably produces a fixed lift remain weak without transparent randomized allocation, verified delivery denominators and downstream booking/revenue outcomes.
- No consequential AI-automation, booking-site, local-acquisition or TikTok development found today changes the Axis offer or approved copy.

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

## Sources checked October 3, 2026
[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414
[3] FTC, CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
[4] Ben-Zion & Lazebnik, Playful AI in Professional Email (2026): https://arxiv.org/abs/2607.11749
[5] Gong, cold-email analysis: https://www.gong.io/blog/does-cold-email-even-work-any-more-heres-what-the-data-says
[6] Lavender, Cold Email Benchmark Report: https://lavender.ai/blog/the-cold-email-benchmark-report
[7] Saleshandy, 2026 benchmark page: https://www.saleshandy.com/blog/cold-email-statistics/

Historical controls and prior evidence remain in Git history. Latest persisted Axis outcome read: `axis-omni-commerce/outreach/runs/2026-10-02-0833-handoff.md`.
