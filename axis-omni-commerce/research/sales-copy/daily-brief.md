# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-07 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision

Preserve the approved control and ordered test queue. **CL-004 remains the only active planned copy test.** CL-005 and CL-008 remain queued, not concurrent. CL-006 and CL-007 remain backlog. Do not change `copy/winners.json`.

Add one measurement guardrail: track bookings independently of replies and report both early and mature outcome windows. This is a BEACON protocol refinement, not a copy winner or deployed campaign change.

The daily ceiling remains **450 confirmed prospect-facing sends**, including first touches, follow-ups and replies, subject to lower eligible inventory and provider capacity.

## Axis evidence observed

- The latest persisted outreach checkpoint remains `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`: **0 confirmed prospect sends / 450**, zero positive replies, zero qualified conversations, zero confirmed bookings/cancellations and no supported revenue.
- Direct Axis Gmail searches covering October 6 through the October 7 review returned **0 Sent messages** and **0 inbox messages**, with no continuation tokens.
- CL-004 still has **0 verified exposures**. No delivered, positive-reply, booking or revenue denominator exists.
- The latest saved inventory remains 15 candidates: 12 verified public-email candidates, two requiring source recheck and one quarantined; AZ 9 / WA 6; sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- Bradley’s owner-authorized mailing address remains stored privately and referenced by `axis-omni-commerce/outreach/sender-config.json`. The historical missing-address block is superseded; current count, recipient, suppression, footer, provider and persistence checks remain mandatory.
- No prospect email, experiment deployment, positive reply, booking, payment or winner is claimed.

## Evidence review

### Verified or strong operational findings

1. **Deliverability and compliance are prerequisites.** Google’s current guidance requires authentication and accurate identity/content, and advises keeping user-reported spam below 0.10% and preventing it from reaching 0.30%. Applicable marketing traffic also requires RFC 8058 one-click-unsubscribe headers; the required body opt-out remains necessary but is not the same mechanism. [1–2]
2. **Reply classes must remain separate.** RevenueFlow manually classified 19,544 replies from 1,413,405 sends. Its platform counter reported 1.38%, while human-written replies were 0.48%; 65.2% of arriving replies were automated. Do not compare unfiltered dashboard reply rates with Axis positive replies. [3]
3. **Failure classes require different action.** Bad addresses, policy blocks, unreachable domains, mailbox-full responses and temporary delay notices are distinct. Quarantine by failure type; never treat a delay notice as a permanent failure while Gmail is retrying. [3]
4. **Open rate remains diagnostic only.** Privacy prefetching and security scanning create machine opens. Axis selects on positive replies, confirmed bookings and downstream revenue.

### New practitioner dataset reviewed October 7

Sales.co published a methodology and results page on October 6 covering 336,257 contacts, 627,085 emails and 20 B2B campaigns. It reports:

- 0.84% human reply rate per contact;
- 0.29% positive reply rate per contact;
- 143 bookings from 124,513 contacts in Sales.co’s own campaign;
- 29% of those bookings came from companies whose contact never replied;
- median booking delay was nine days, but 34% arrived more than 30 days after first touch;
- seven of 143 booked companies had become paying customers by October 6.

The page separates contacts from emails, automated from human replies, and bookings from attributed bookings. It also acknowledges that email preceding a booking does not prove causation, that meeting data covers only the vendor’s own campaign, and that revenue is immature with only seven customers. This is transparent observational evidence—not an Axis benchmark and not a randomized copy study. [4]

**Operational implication:** BEACON must reconcile calendar bookings separately from reply labels. A no-reply prospect can still book. Thirty-day bookings are an early read, not a mature total.

### Practitioner findings retained as hypotheses only

- Sales.co’s separate 1,279,153-contact personalization analysis found lower positive replies for AI-personalized first lines than for templates, but same-client human-reply comparisons were split 10–9. This continues to motivate CL-004, not a generic-copy winner claim. [5]
- Gong associates concise subjects/bodies and concrete value offers with better outcomes in large vendor datasets, but public summaries do not establish recipient-level randomization or complete denominators. These findings motivate CL-005 and CL-007 only. [6–7]
- Lavender’s 231,818-email sample is contextual; its reported lift is entangled with a proprietary score and self-selected users. [8]

### Weak or rejected claims

- RevenueFlow’s CTA page explicitly describes its ranges as compiled industry estimates rather than a controlled dataset. Its 6–12% “simple question” figures and fixed CTA lifts are not acceptable Axis benchmarks. [9]
- Do not compare sources that count contacts, emails or campaigns differently, or combine positive, neutral and automated replies.
- Fixed lifts for first-name tokens, “quick question,” a particular subject length, universal word count or follow-up count remain weak without randomized allocation and downstream denominators.
- No consequential AI-automation, booking-site, local-acquisition or TikTok development found today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable, sourced situational detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain-text copy with Bradley’s identity, approved offer, complete footer and exact opt-out.

These are operational controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact versions. Hold eligibility, offer, pricing, sender, subject, cadence and compliance constant except for the named variable. Deduplicate by business and recipient.

Measure:

- positive replies within 14 days;
- early confirmed bookings within 30 days;
- mature confirmed bookings within 60 days;
- supported revenue at 60 days as interim and 90 days as mature;
- opt-outs, complaints and verified failure classes as guardrails.

Track bookings independently of replies and preserve attribution source when available. Autoreplies, neutral replies, negative replies and opt-outs are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent and mark delivery unknown.

**Sample P:** after the first Axis baseline is observed, calculate per-version sample size for a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until then, 200–400 eligible recipients per version is only a feasibility pilot.

**Rule K:** keep only when the primary endpoint’s 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to bookings, revenue, opt-outs, complaints or bounces. Retire when the interval rules out that effect. Otherwise label inconclusive. Never declare a winner before the relevant outcome window matures. Safety stops override sample completion.

## Ordered hypotheses

| Order / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample requirement | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Current approved AI/automation-led opener | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | 30/60-day bookings, qualified conversations, 60/90-day revenue/contact, opt-outs | P | K; immediate kill for fabricated, stale or unsupported relevance |
| 2 / CL-005 | Current discovery question | Offer to share two concrete observations; booking link remains secondary in both | Positive replies / eligible recipients | 30/60-day bookings, qualified conversations, 60/90-day revenue/contact | P after CL-004 endpoint | K; reject if reply lift fails to improve downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized nonresponders | Incremental 30/60-day bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop sequence on any human reply, opt-out, bounce or complaint |
| Backlog / CL-006 | Existing body length | 50–80 words; proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after prior endpoint | K; skip if control is already in range |
| Backlog / CL-007 | Existing truthful subject | Truthful 1–4-word priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after prior endpoint | K; never select on opens alone |

## Executable handoff

1. Record this file’s date and blob SHA. Reconcile fully paginated Axis Gmail Sent with durable history; check inbox, suppressions, drafts, thread state, failures, bookings and current provider state.
2. Read the private sender-address reference and render the complete compliant footer before sending. Never expose unresolved placeholders or copy the private address into public research files.
3. Use the preserved control outside active CL-004 allocation. Keep sticky STAN/CUSTOMER_SERVICE/BRIDGE assignments.
4. For CL-004 only, randomize eligible first-touch businesses within state × niche × arm. Persist assignment, exact version, Gmail message ID and accepted/delivery state immediately.
5. Do not begin CL-005 concurrently with CL-004. Do not begin CL-008 until an eligible nonresponder cohort and approved due date exist.
6. Reconcile booking confirmations even when the prospect never replied. Distinguish booked, cancelled, attended and attributed-source states.
7. Objections: opt-out/not interested → suppress without rebuttal; timing → acknowledge and obtain permission for a later date; price → use verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
8. Process sequential batches of 15–25 with count, suppression and provider checks between batches. Never exceed 450 and never force volume through weak leads or provider limits.
9. BEACON reports state × niche × arm × hypothesis with numerators, denominators, observation windows and intervals. Positive replies, confirmed bookings and revenue outrank opens. Unknown delivery remains unknown.
10. January/Infoton remains excluded. Do not automatically email January or reactivate the Infoton watch.

## Copy-library decision

**No new copy finding is strong enough to add as an approved winner.** Add only the measurement guardrail to operating practice: bookings must be reconciled independently of replies and reported at both 30- and 60-day windows. Preserve the candidate copy structure for testing: sourced observation → possible useful outcome → concrete value offer → secondary booking path.

Do not add generic AI praise, benchmark promises, deceptive urgency, fake familiarity or autonomous-AI claims.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 7, 2026

[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126  
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414  
[3] RevenueFlow, Cold Email Benchmarks 2026, data through August 12, 2026: https://www.revenueflow.com/benchmarks/cold-email-benchmark-report-2026  
[4] Sales.co, Cold Email Conversion Rate Benchmarks for B2B, published October 6, 2026: https://sales.co/research/cold-email-conversion-rate-benchmarks  
[5] Sales.co, Personalization no longer matters for cold email, September 27, 2026: https://sales.co/research/personalization-no-longer-matters  
[6] Gong, How to master cold email: https://www.gong.io/resources/guides/how-to-master-cold-email-get-the-data-backed-guide-based-on-85-million-emails  
[7] Gong, executive cold-email analysis: https://www-vercel.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says  
[8] Lavender, Cold Email Benchmark Report, updated March 30, 2026: https://lavender.ai/blog/the-cold-email-benchmark-report  
[9] RevenueFlow, Cold Email CTA Benchmarks, updated October 1, 2026: https://www.revenueflow.com/blog/cold-email-cta-benchmarks

Historical evidence, prior briefs and approved controls remain in Git history. Latest persisted Axis outcome read: `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`.
