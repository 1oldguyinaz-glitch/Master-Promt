# COPY LAB — Daily Sales-Copy Brief
Date: 2026-09-30 (Pacific)
Status: RESEARCH AND VERIFIED REPOSITORY HANDOFF; ALL NEW TESTS UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision
Preserve the existing control and keep **CL-004 as the only active copy hypothesis once sending is legally and operationally eligible**. Do not promote a winner from vendor benchmarks or small Axis samples. The daily ceiling is 450 prospect-facing sends, including first touches, follow-ups and replies, subject to lower provider capacity. This brief does not prove sending recovery.

## Axis evidence observed before this handoff
- The 2026-09-30 outreach checkpoints report **0 confirmed prospect sends / 450**, zero positive prospect replies, zero qualified conversations and zero confirmed bookings/cancellations. Payments/revenue were not queried. With no current denominator, no Axis copy effect can be estimated.
- Queue: 15 saved candidates; 12 have public business-email page confirmation, two require source recheck, and one is quarantined for a source mismatch. AZ 9 / WA 6 and sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5 remain unchanged.
- Gmail authentication works, but no valid Axis physical postal address appears in the repository. Every queued draft remains blocked and marked do-not-send. This is a compliance blocker, not a copy problem.
- One Uber support acknowledgment was processed as an internal operational message, not a lead or prospect reply. No sales response was sent.
- No experiment was deployed and no winner changed.

## Verified findings and limitations
1. **Deliverability and truthful identity are stronger than copy folklore.** Google requires accurate sender/subject representation, authentication, monitoring and low complaint rates; it advises keeping Postmaster spam rates below 0.10% and avoiding 0.30% or higher. FTC guidance requires accurate headers/subjects, ad identification, opt-out capability and a valid physical postal address; a properly registered P.O. box or private mailbox can qualify. These are operational guardrails, not conversion hypotheses. [1–4]
2. **A new large vendor dataset is useful context, not causal proof.** Saleshandy says it aggregated 53.1M cold emails and 60,000 sequences from January–June 2026. It reports a 3.7% total reply average, 44.5% of positive replies occurring on follow-ups, and stronger results in smaller segmented sequences and 50–80-word first emails. Campaigns were grouped rather than randomized, industries and list quality differ, and several published positive-reply figures are internally difficult to reconcile. Do not use its percentages as Axis forecasts or proof that length/follow-up caused the result. [5]
3. **Vendor AI-vs-human results are weak evidence.** A Saleshandy case study reports AI-only, human-only and hybrid outcomes, including 4.1% total replies, 1.4% positive replies and 0.7% meetings for one 5,000-email AI-only campaign, with higher reported hybrid results. The article does not establish randomized assignment or equivalent audiences and is product-linked. Treat “AI research plus final judgment” as a quality-control rationale, not a measured Axis winner. [6]
4. **Adjacent field evidence does not show a direct tone lift.** A 2026 randomized crossover field experiment across 16,880 ordinary workplace emails found playful/professional AI rewrites changed measured tone but did not directly change opens, replies or response time. This is not cold outreach to local businesses, so it argues against prioritizing a tone-only test, not against all tone effects. [7]
5. Prior Woodpecker and Gong findings remain contextual: observational reply benchmarks, short subjects, concise bodies, relevant openings and concrete value offers are candidates, not universal rules. No new evidence today upgrades them to library winners. [8–10]

## Controls and hypotheses
Preserve CL-001 situational relevance, CL-002 one discovery CTA plus secondary booking link, and CL-003 concise copy as recorded controls—not proven winners. CL-004 through CL-008 remain unproven. Defer CL-005 through CL-008 until CL-004 reaches its preregistered endpoint. Do not add a tone-only test.

Common design: randomize by business; stratify by state, niche and sticky arm; freeze the exact control/version before sending; keep eligibility, offer, pricing, sender, cadence and compliance identical; deduplicate businesses. Primary window: 14 days for positive replies, 30 days for bookings, 60 days for revenue. Autoreplies, opt-outs and negative replies are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent.

**Sample requirement P:** calculate from the observed Axis baseline and a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until a baseline exists, any 200–400-per-version run is a feasibility pilot only.  
**Decision K:** keep only if the endpoint 95% interval excludes zero and reaches the worthwhile effect without material booking/revenue, opt-out, complaint or bounce harm. If the interval rules out the worthwhile effect, retire; otherwise mark inconclusive and retain control. Safety stops override sample completion.

| ID | Control | Variant / hypothesis | Primary metric | Secondary metrics | Sample | Kill / keep |
|---|---|---|---|---|---|---|
| CL-004 | Existing AI/automation-led opening | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings, qualified conversations, revenue/contact, opt-outs | P | K; kill immediately for fabricated or unsupported relevance |
| CL-005 | Existing discovery question | Concrete offer to share two useful observations; booking link secondary in both | Positive replies / recipients | Bookings, qualified conversations, revenue/contact, opt-outs | P after CL-004 | K; reject if added replies do not improve downstream quality |
| CL-006 | Actual existing body length | 50–80 words, proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after CL-004 | K; skip if control is already in range |
| CL-007 | Actual existing subject | Truthful 1–4-word priority subject; body fixed | Positive replies / recipients | Bookings, revenue/contact; opens diagnostic only | P after CL-004 | K; never select on opens alone |
| CL-008 | No follow-up | One useful follow-up after five business days to eligible randomized nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints, extra sends | P using nonresponder baseline | K; stop on reply/opt-out/bounce; vendor sequence shares do not prove causality |

## Executable handoff
1. **Compliance gate:** do not send until a verified current Axis street address, registered P.O. box or registered private mailbox is present in sender configuration and the footer. Never infer Bradley's home address.
2. Read and record this file's date and SHA. Reconcile paginated Gmail Sent and durable history; recheck inbox, suppressions and failure quarantines.
3. When eligible, use the existing control outside CL-004. Day zero: Bradley identity, one sourced relevance point, possible outcome without promises, one primary question, secondary 15-minute booking link and exact opt-out.
4. CL-004 only: randomize qualified first-touch businesses within state × niche × sticky arm. Persist assignment, exact copy version, Gmail ID and accepted/delivery state.
5. Follow up only when due under an approved sequence or CL-008 assignment; add a new useful observation rather than repeating pressure. Stop on any human reply, opt-out, bounce or complaint.
6. Objections: opt-out/not interested → suppress with no rebuttal; timing → acknowledge and obtain permission for a later date; price → answer only with verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
7. Process sequential batches of 15–25, rechecking live count, suppression and provider responses between batches. Never exceed 450. Do not force volume through weak leads or provider limits.
8. BEACON reports state × niche × arm × hypothesis with numerators, denominators and intervals. Positive replies, bookings and revenue outrank opens. Unknown delivery remains unknown.

## Copy library decision
**No new finding is strong enough to add as an approved winner.** Retain only the existing unproven candidate pattern: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Do not add unsupported case studies, quantified savings, fake familiarity, generic local-color personalization or autonomous AI copy claims.

Required secondary booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

Do not modify `copy/winners.json` without measured Axis evidence.

## Sources checked September 30, 2026
[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126  
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414  
[3] FTC, CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business  
[4] FTC, 2008 rule provision on registered P.O. boxes/private mailboxes: https://www.ftc.gov/news-events/news/press-releases/2008/05/ftc-approves-new-rule-provision-under-can-spam-act  
[5] Saleshandy, 53.1M-email 2026 benchmark: https://www.saleshandy.com/blog/cold-email-statistics/  
[6] Saleshandy, AI vs human outreach case study: https://www.saleshandy.com/blog/ai-vs-human-cold-emails/  
[7] Ben-Zion & Lazebnik, *Playful AI in Professional Email* (2026 preprint): https://arxiv.org/abs/2607.11749  
[8] Woodpecker cold-email benchmarks: https://woodpecker.co/cold-email-benchmarks/  
[9] Woodpecker A/B planning calculator: https://woodpecker.co/cold-email-ab-test-calculator/  
[10] Gong, executive cold-email analysis (2026): https://dev.www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says

Historical controls and prior evidence remain in Git history. Latest outcome records read: `axis-omni-commerce/outreach/runs/2026-09-30-0030-reconciliation.md`, `2026-09-30-0734-inbox.md`, and `2026-09-29-2330-verification.md`.
