# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-01 (Pacific)
Status: RESEARCH AND VERIFIED REPOSITORY HANDOFF; ALL NEW TESTS UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision
Preserve the current control. **CL-004 remains the only planned copy test once outreach is legally and operationally eligible.** No campaign winner changes today. The daily ceiling remains 450 prospect-facing sends, including first touches, follow-ups and replies, subject to lower provider capacity.

## Axis evidence observed
- No 2026-10-01 outreach outcome record was present at research time. The latest persisted records remain the 2026-09-30 reconciliation and inbox records.
- Latest persisted outcome: **0 confirmed prospect sends / 450**, zero positive prospect replies, zero qualified conversations and zero confirmed bookings/cancellations. No current copy denominator exists.
- The saved queue remains 15 candidates: 12 public business-email sources confirmed, two requiring source recheck and one quarantined for a source mismatch; AZ 9 / WA 6 and sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- Gmail connectivity was previously verified, but the repository still contains no verified Axis physical postal address. New marketing sends remain blocked. This is a compliance condition, not a copy-performance diagnosis.
- No experiment was deployed and no winner changed.

## Evidence review
### Verified or strong operational findings
1. **Compliance and deliverability outrank copy tweaks.** Google requires truthful identity and subject representation, authentication, monitoring and low complaint rates; its guidance says to keep Postmaster spam rates below 0.10% and avoid 0.30% or higher. FTC guidance requires accurate headers/subjects, a working opt-out and a valid physical postal address; an accurately registered P.O. box or private mailbox can qualify. These are guardrails, not conversion hypotheses. [1–4]
2. **Open rate is diagnostic, not a selection metric.** Privacy and proxy loading can make opens unreliable. Axis selects on positive replies, booked meetings per delivered email and downstream revenue. Practitioner benchmark pages support this priority, but their exact percentages are not causal or transferable to Axis. [5–7]
3. **Tone-only rewriting remains deprioritized.** A 2026 randomized crossover field experiment across 16,880 workplace emails changed measured tone but found no direct effect on opens, replies or response time. This population was not cold local-business outreach, so the result does not prove tone never matters; it only weakens the case for testing tone before relevance and offer structure. [8]

### Useful but weak claims
- Large vendor datasets commonly associate concise bodies, relevant openings, small segmented lists and follow-ups with higher replies. They are grouped observational results with uncontrolled list quality, offer, industry and deliverability. Treat these as hypothesis generators, not Axis forecasts. [5–7, 9–11]
- Claims that personalized subject lines create double-digit lifts are frequently repeated through secondary vendor articles without a transparent randomized source. Do not add such a lift to planning assumptions.
- A new large phishing-content study is useful for security awareness but not evidence about ethical B2B response behavior. Do not borrow urgency, impersonation or deceptive CTA patterns. [12]

## Controls and hypotheses
Preserve CL-001 sourced situational relevance, CL-002 one discovery CTA plus secondary booking link, and CL-003 concise copy as controls—not proven winners. CL-004 through CL-008 remain unproven. Defer CL-005 through CL-008 until CL-004 reaches its preregistered endpoint.

Common design: randomize by business; stratify by state, niche and sticky arm; freeze exact control/version; keep eligibility, offer, pricing, sender, cadence and compliance identical; deduplicate businesses. Primary windows: 14 days positive replies, 30 days bookings, 60 days revenue. Autoreplies, opt-outs and negative replies are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent.

**Sample P:** calculate from the observed Axis baseline and a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until a baseline exists, 200–400 per version is only a feasibility pilot.  
**Rule K:** keep only when the endpoint 95% interval excludes zero and reaches the worthwhile effect without material harm to bookings/revenue, opt-outs, complaints or bounces. Retire when the interval rules out the worthwhile effect; otherwise mark inconclusive. Safety stops override sample completion.

| ID | Control | Variant / hypothesis | Primary metric | Secondary metric | Sample | Kill / keep |
|---|---|---|---|---|---|---|
| CL-004 | Existing AI/automation-led opening | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings, qualified conversations, revenue/contact, opt-outs | P | K; kill immediately for fabricated or unsupported relevance |
| CL-005 | Existing discovery question | Offer to share two useful observations; booking link secondary in both | Positive replies / recipients | Bookings, qualified conversations, revenue/contact | P after CL-004 | K; reject if reply lift does not improve downstream quality |
| CL-006 | Existing body length | 50–80 words; proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after CL-004 | K; skip if control is already in range |
| CL-007 | Existing subject | Truthful 1–4-word priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after CL-004 | K; never select on opens alone |
| CL-008 | No follow-up | One useful follow-up after five business days to eligible randomized nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from nonresponder baseline | K; stop on any reply, opt-out, bounce or complaint |

## Executable handoff
1. Do not send until a verified current Axis street address, registered P.O. box or registered private mailbox is in sender configuration and the footer. Never infer Bradley’s home address.
2. Record this file’s date and SHA. Reconcile paginated Gmail Sent with durable history; check inbox, suppressions, drafts, thread state and failure quarantines.
3. Use the existing control outside CL-004. First touch: Bradley identity, one sourced relevance point, possible outcome without promises, one primary question, secondary booking link and exact opt-out.
4. For CL-004 only, randomize eligible first-touch businesses within state × niche × sticky arm. Persist assignment, exact copy version, Gmail ID and accepted/delivery state.
5. Follow up only when due under an approved sequence or CL-008 assignment. Add useful information rather than repeating pressure. Stop on any human reply, opt-out, bounce or complaint.
6. Objections: opt-out/not interested → suppress without rebuttal; timing → acknowledge and obtain permission for a later date; price → use verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
7. Process sequential batches of 15–25, rechecking count, suppression and provider responses between batches. Never exceed 450 and never force volume through weak leads or provider limits.
8. BEACON reports state × niche × arm × hypothesis with numerators, denominators and intervals. Positive replies, bookings and revenue outrank opens. Unknown delivery remains unknown.

## Copy-library decision
**No new finding is strong enough to add as an approved winner.** Preserve the existing candidate pattern only: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Do not add unsupported quantified savings, fake familiarity, generic local-color personalization, deceptive urgency or autonomous-AI claims.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

Do not modify `copy/winners.json` without measured Axis evidence.

## Sources checked October 1, 2026
[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126  
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414  
[3] FTC, CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business  
[4] FTC, registered P.O. boxes/private mailboxes: https://www.ftc.gov/news-events/news/press-releases/2008/05/ftc-approves-new-rule-provision-under-can-spam-act  
[5] Saleshandy, 53.1M-email 2026 benchmark: https://www.saleshandy.com/blog/cold-email-statistics/  
[6] Instantly, 2026 reply-rate benchmark: https://instantly.ai/blog/cold-email-reply-rate-benchmarks/  
[7] Martal, 2026 metrics/benchmark synthesis: https://martal.ca/cold-email-metrics/  
[8] Ben-Zion & Lazebnik, *Playful AI in Professional Email* (2026 preprint): https://arxiv.org/abs/2607.11749  
[9] Woodpecker cold-email benchmarks: https://woodpecker.co/cold-email-benchmarks/  
[10] Woodpecker A/B planning calculator: https://woodpecker.co/cold-email-ab-test-calculator/  
[11] Gong, executive cold-email analysis: https://dev.www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says  
[12] Park et al., *A Large-Scale Empirical Study of Modern Phishing Email Content* (2026 preprint): https://arxiv.org/abs/2609.30683

Historical controls and prior evidence remain in Git history. Latest persisted outcomes read: `axis-omni-commerce/outreach/runs/2026-09-30-0030-reconciliation.md`, `2026-09-30-0734-inbox.md`, and `2026-09-29-2330-verification.md`.
