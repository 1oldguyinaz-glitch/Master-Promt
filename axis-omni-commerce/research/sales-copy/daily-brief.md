# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-05 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision

Preserve the approved control and do not change `copy/winners.json`. Run at most one copy variable at a time. The ranked Monday queue is:

1. **CL-004 now:** sourced operational observation versus the current AI/automation-led opener.
2. **CL-005 next:** concrete value offer versus the current discovery question.
3. **CL-008 after first-touch measurement:** one useful day-5 follow-up versus no follow-up.

CL-006 and CL-007 remain backlog. These rankings are test priorities, not winner claims. The daily ceiling remains **450 confirmed prospect-facing sends**, including first touches, follow-ups and replies, subject to lower eligible inventory and provider capacity.

## Axis evidence observed

- The latest persisted outreach checkpoint is `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`. It reports **0 confirmed prospect sends / 450**, zero positive replies, zero qualified conversations, zero confirmed bookings/cancellations and no supported revenue.
- A direct Axis Gmail reconciliation for October 3 through October 5 found no Sent or inbox messages and no continuation token. Therefore CL-004 still has **0 exposures**, and no Axis copy denominator exists.
- The saved candidate inventory at the latest checkpoint was 15: 12 verified public-email candidates, two requiring source recheck and one quarantined; AZ 9 / WA 6; sticky STAN 5 / CUSTOMER_SERVICE 5 / BRIDGE 5.
- Bradley’s owner-authorized mailing address is now stored privately and referenced by `axis-omni-commerce/outreach/sender-config.json`. This supersedes the historical missing-address block, but does not by itself prove postal validation, sending eligibility, delivery or deployment.
- No prospect email, experiment deployment, positive reply, booking, payment or campaign winner is claimed.

## Evidence review

### Verified or strong operational findings

1. **Deliverability and compliance outrank copy optimization.** Google’s sender guidance requires authentication, accurate sender identity and content, valid DNS, TLS, low spam rates and gradual volume increases. Google advises keeping Postmaster spam below 0.10% and avoiding 0.30% or higher. Applicable bulk traffic also requires DMARC alignment and one-click unsubscribe. FTC requirements remain applicable to commercial B2B email: accurate headers and subjects, ad identification, a valid physical postal address, a clear opt-out and timely suppression. These are guardrails, not conversion hypotheses. [1–3]
2. **Open rate is diagnostic only.** Privacy prefetching and security scanners can create machine opens. Axis selects on positive replies per eligible recipient, booked meetings per delivered email and downstream revenue.
3. **Human reply definitions matter.** RevenueFlow’s published 2026 dataset reports 0.48% human replies across 1,413,405 sends after excluding automated replies, versus 1.38% from the platform reply counter. Its 356 campaigns were overwhelmingly one-touch. This is useful evidence against comparing unfiltered dashboard reply rates, but it is one vendor’s population and is not an Axis performance target. [4]
4. **Vendor datasets support test design, not causal rules.** Gong reports analyses ranging from 300,000 to 85 million cold emails; Lavender’s current benchmark sampled 231,818 emails and explicitly warns that offers differ. The public summaries do not establish recipient-level randomized causality for Axis. [5–7]

### Current practitioner finding: useful, not proven

Sales.co published data on 1,279,153 contacts first emailed from April 2025 through September 25, 2026. AI-personalized first lines had 0.15% positive replies, plain templates 0.56%, and randomized non-personal components 0.22%. Same-client comparisons were mixed: personalization won human reply rate in 10 of 19 clients, while templates won in nine. The authors disclose changing client mix, unequal samples, recency/censoring, follow-up attribution and single-tool selection limits. This is transparent observational evidence that AI-written profile praise is not automatically valuable—not proof that generic copy wins. It strengthens CL-004’s rationale: test sourced business relevance against the current opener and never treat synthetic personalization as a control fact. [8]

### Weak or rejected claims

- Fixed lifts for first-name tokens, “quick question,” a particular subject length, a specific word count or a universal number of follow-ups remain weak without randomized assignment, delivery denominators and downstream outcomes.
- Gong’s current executive analysis associates 1–4-word subjects, 50–100-word bodies and concrete value offers with better outcomes, but its public article does not expose randomization or full denominators. Use it to motivate CL-005/CL-007, not as a library rule. [6]
- Lavender’s score-based lift is entangled with its proprietary scoring model and self-selected users. It is a segment benchmark, not causal evidence that earning a score causes replies. [7]
- No consequential AI-automation, booking-site, local-acquisition or TikTok development found today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable, sourced situational detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain-text copy with Bradley’s identity, approved offer, required footer and exact opt-out.

These are operational controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact copy versions. Hold eligibility, offer, pricing, sender, subject, cadence and compliance constant except for the named variable. Deduplicate by business and recipient. Count positive replies within 14 days, confirmed bookings within 30 days and supported revenue within 60 days. Autoreplies, opt-outs and negative replies are not positive replies. Use delivered denominators only when delivery is verified; otherwise report accepted/sent and mark delivery unknown.

**Sample P:** after the first Axis baseline is observed, calculate per-version sample size for a preregistered worthwhile absolute lift using a two-sided 0.05 alpha and 80% power. Until then, 200–400 eligible recipients per version is a feasibility pilot, not a powered winner test.

**Rule K:** keep only when the primary endpoint’s 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to booked meetings, revenue, opt-outs, complaints or bounces. Retire when the interval rules out that effect. Otherwise label inconclusive. Safety stops override sample completion.

## Monday’s three highest-leverage tests

| Rank / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample requirement | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Current approved AI/automation-led opener | One sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings/delivered, qualified conversations, revenue/contact, opt-outs | P | K; immediate kill for fabricated, stale or unsupported relevance |
| 2 / CL-005 | Current discovery question | Offer to share two concrete observations; booking link remains secondary in both | Positive replies / eligible recipients | Bookings/delivered, qualified conversations, revenue/contact | P after CL-004 endpoint | K; reject if reply lift fails to improve downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop sequence on any human reply, opt-out, bounce or complaint |

## Executable handoff

1. Record this file’s date and blob SHA. Reconcile paginated Axis Gmail Sent with durable history; check inbox, suppressions, drafts, thread state, failures and current provider state.
2. Read the private sender address reference and render the complete compliant footer before any send. Never expose unresolved placeholders or copy the private address into public research files.
3. Use the preserved control outside the active CL-004 allocation. Keep sticky STAN/CUSTOMER_SERVICE/BRIDGE assignments.
4. For CL-004 only, randomize eligible first-touch businesses within state × niche × arm. Persist assignment, exact copy version, accepted/delivery state and Gmail message ID immediately.
5. Do not begin CL-005 concurrently with CL-004. Do not begin CL-008 until the eligible nonresponder cohort and approved timing are known.
6. Objections: opt-out/not interested → suppress without rebuttal; timing → acknowledge and obtain permission for a later date; price → use verified scope/pricing and one clarification; existing provider → acknowledge without inventing deficiencies.
7. Process sequential batches of 15–25 with count, suppression and provider checks between batches. Never exceed 450; never force volume through weak leads or provider limits.
8. BEACON reports state × niche × arm × hypothesis with numerators, denominators and intervals. Positive replies, confirmed bookings and revenue outrank opens. Unknown delivery remains unknown.

## Copy-library decision

**No new finding is strong enough to add as an approved winner.** Preserve only the candidate structure for testing: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Do not add generic AI praise, benchmark promises, deceptive urgency, fake familiarity or autonomous-AI claims.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 5, 2026

[1] Google, Email sender guidelines: https://support.google.com/mail/answer/81126  
[2] Google, Email sender guidelines FAQ: https://support.google.com/mail/answer/14229414  
[3] FTC, CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business  
[4] RevenueFlow, Cold Email Benchmarks 2026, data through August 12, 2026: https://www.revenueflow.com/benchmarks/cold-email-benchmark-report-2026  
[5] Gong, How to master cold email, analysis of 85 million emails: https://www.gong.io/resources/guides/how-to-master-cold-email-get-the-data-backed-guide-based-on-85-million-emails  
[6] Gong, executive cold-email analysis: https://www-vercel.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says  
[7] Lavender, Cold Email Benchmark Report, updated March 30, 2026: https://lavender.ai/blog/the-cold-email-benchmark-report  
[8] Sales.co, Personalization no longer matters for cold email, September 27, 2026: https://sales.co/research/personalization-no-longer-matters

Historical evidence, prior briefs and approved controls remain in Git history. Latest persisted Axis outcome read: `axis-omni-commerce/outreach/runs/2026-10-03-0825-handoff.md`.
