# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-06 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision

Preserve the approved control and the ordered test queue. **CL-004 remains the only active planned copy test.** CL-005 and CL-008 remain queued, not concurrent. CL-006 and CL-007 remain backlog. Do not change `copy/winners.json`.

No new evidence today supports a campaign winner or offer change. The daily ceiling remains **450 confirmed prospect-facing sends**, including first touches, follow-ups and replies, subject to lower eligible inventory and provider capacity.

## Axis evidence observed

- The latest persisted outreach checkpoint remains `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`: **0 confirmed prospect sends / 450**, zero positive replies, zero qualified conversations, zero confirmed bookings/cancellations and no supported revenue.
- Direct Axis Gmail searches covering October 5 through the October 6 review returned **0 Sent messages** and **0 inbox messages**, with no continuation tokens.
- CL-004 therefore still has **0 verified exposures**. No delivered denominator, positive-reply denominator, booking denominator or revenue denominator exists.
- The latest saved candidate inventory remains 15: 12 verified public-email candidates, two requiring source recheck and one quarantined; AZ 9 / WA 6; sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- Bradley’s owner-authorized mailing address remains stored privately and referenced by `axis-omni-commerce/outreach/sender-config.json`. The historical missing-address block is superseded, while all current count, recipient, suppression, footer, provider and persistence checks remain mandatory.
- No prospect email, experiment deployment, positive reply, booking, payment or campaign winner is claimed.

## Evidence review

### Verified or strong operational findings

1. **Deliverability and compliance remain prerequisites.** Google’s current FAQ says sender-guideline enforcement can cause temporary or permanent rejection or spam placement. It requires authentication and accurate sender identity/content, and advises keeping user-reported spam below 0.10% and preventing it from reaching 0.30%. Applicable marketing traffic also requires RFC 8058 one-click unsubscribe headers; a body-only opt-out line is not the same mechanism. [1–2]
2. **Positive replies must be separated from other replies.** RevenueFlow manually classified 19,544 replies from 1,413,405 sends. Its platform counter reported 1.38%, while human-written replies were 0.48%; 65.2% of arriving replies were automated. This supports Axis’s existing rule to exclude autoresponses and report explicit reply classes. It does not establish a conversion target for Axis. [3]
3. **Bounce classes require different actions.** RevenueFlow’s same dataset separates bad addresses, blocked/policy rejections, unreachable domains, mailbox-full responses and temporary delay notices. Axis should quarantine by failure type and never treat a delay notice as a verified permanent failure while Gmail is still retrying. [3]
4. **Open rate remains diagnostic only.** Privacy prefetching and security scanning can create machine opens. Axis selects on positive replies per eligible recipient, confirmed bookings per verified delivered email and downstream revenue.

### Practitioner findings: useful, not causal

- Sales.co’s 1,279,153-contact observational analysis found lower positive replies for AI-personalized first lines than for plain templates, but same-client human-reply comparisons were split 10–9. Unequal samples, changing client mix, censoring and follow-up attribution prevent a causal conclusion. This continues to motivate CL-004—sourced business relevance versus the current opener—not a rule that generic copy wins. [4]
- Gong associates short subjects, 50–100-word bodies and concrete value offers with higher outcomes in large vendor datasets. Public summaries do not establish recipient-level randomization or expose all relevant denominators. These findings motivate CL-005 and CL-007 only. [5–6]
- Lavender’s 231,818-email sample is useful context, but its score-based lift is entangled with a proprietary scoring system and self-selected users. Lavender itself cautions that offers differ. [7]

### New benchmark reviewed October 6

Nerolead’s October 2026 page publishes reply and attended-meeting rates across 251 campaigns and defines its sample as campaigns, not contacts. Its “reply” metric combines positive and neutral replies, its sectors exclude local service businesses, and it does not publish recipient counts for each cell or randomized copy allocation. The headline 11.2% median is across channels rather than a cold-email-only Axis comparator. Treat the page as weak directional context only; do not import its rates as Axis goals or library claims. [8]

### Weak or rejected claims

- Do not compare rates when one source counts contacts, another counts emails, another counts campaigns, or another combines positive, neutral and automated replies.
- Fixed lifts for first-name tokens, “quick question,” a particular subject length, a universal word count or a universal follow-up count remain weak without randomized allocation, delivery denominators and downstream outcomes.
- No consequential AI-automation, booking-site, local-acquisition or TikTok development found today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable, sourced situational detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain-text copy with Bradley’s identity, approved offer, complete footer and exact opt-out.

These are operational controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact copy versions. Hold eligibility, offer, pricing, sender, subject, cadence and compliance constant except for the named variable. Deduplicate by business and recipient.

Measure:

- positive replies within 14 days;
- confirmed bookings within 30 days;
- supported revenue within 60 days;
- opt-outs, complaints and verified failure classes as guardrails.

Autoreplies, neutral replies, negative replies and opt-outs are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent and mark delivery unknown.

**Sample P:** after the first Axis baseline is observed, calculate the per-version sample for a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until then, 200–400 eligible recipients per version is only a feasibility pilot.

**Rule K:** keep only when the primary endpoint’s 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to bookings, revenue, opt-outs, complaints or bounces. Retire when the interval rules out that effect. Otherwise label inconclusive. Safety stops override sample completion.

## Ordered hypotheses

| Order / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample requirement | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Current approved AI/automation-led opener | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings/delivered, qualified conversations, revenue/contact, opt-outs | P | K; immediate kill for fabricated, stale or unsupported relevance |
| 2 / CL-005 | Current discovery question | Offer to share two concrete observations; booking link remains secondary in both | Positive replies / eligible recipients | Bookings/delivered, qualified conversations, revenue/contact | P after CL-004 endpoint | K; reject if reply lift fails to improve downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop sequence on any human reply, opt-out, bounce or complaint |
| Backlog / CL-006 | Existing body length | 50–80 words; proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after prior endpoint | K; skip if control is already in range |
| Backlog / CL-007 | Existing truthful subject | Truthful 1–4-word priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after prior endpoint | K; never select on opens alone |

## Executable handoff

1. Record this file’s date and blob SHA. Reconcile fully paginated Axis Gmail Sent with durable history; check inbox, suppressions, drafts, thread state, failures and current provider state.
2. Read the private sender-address reference and render the complete compliant footer before sending. Never expose unresolved placeholders or copy the private address into public research files.
3. Use the preserved control outside the active CL-004 allocation. Keep sticky STAN/CUSTOMER_SERVICE/BRIDGE assignments.
4. For CL-004 only, randomize eligible first-touch businesses within state × niche × arm. Persist assignment, exact version, Gmail message ID and accepted/delivery state immediately.
5. Do not begin CL-005 concurrently with CL-004. Do not begin CL-008 until an eligible nonresponder cohort and approved due date exist.
6. Objections: opt-out/not interested → suppress without rebuttal; timing → acknowledge and obtain permission for a later date; price → use verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
7. Process sequential batches of 15–25 with count, suppression and provider checks between batches. Never exceed 450 and never force volume through weak leads or provider limits.
8. BEACON reports state × niche × arm × hypothesis with numerators, denominators and intervals. Positive replies, confirmed bookings and revenue outrank opens. Unknown delivery remains unknown.
9. January/Infoton remains excluded. Do not automatically email January or reactivate the Infoton watch.

## Copy-library decision

**No new finding is strong enough to add as an approved winner.** Preserve only the candidate structure for testing: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Do not add generic AI praise, benchmark promises, deceptive urgency, fake familiarity or autonomous-AI claims.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 6, 2026

[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126  
[2] Google, Email sender guidelines FAQ, reviewed October 6, 2026: https://support.google.com/mail/answer/14229414  
[3] RevenueFlow, Cold Email Benchmarks 2026, data through August 12, 2026: https://www.revenueflow.com/benchmarks/cold-email-benchmark-report-2026  
[4] Sales.co, Personalization no longer matters for cold email, September 27, 2026: https://sales.co/research/personalization-no-longer-matters  
[5] Gong, How to master cold email, analysis of 85 million emails: https://www.gong.io/resources/guides/how-to-master-cold-email-get-the-data-backed-guide-based-on-85-million-emails  
[6] Gong, executive cold-email analysis: https://www-vercel.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says  
[7] Lavender, Cold Email Benchmark Report, updated March 30, 2026: https://lavender.ai/blog/the-cold-email-benchmark-report  
[8] Nerolead, 2026 B2B outbound benchmarks, reviewed October 6, 2026: https://nerolead.com/resources/benchmarks

Historical evidence, prior briefs and approved controls remain in Git history. Latest persisted Axis outcome read: `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`.
