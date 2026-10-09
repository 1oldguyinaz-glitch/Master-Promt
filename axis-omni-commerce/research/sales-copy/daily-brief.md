# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-09 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis Washington Business Hours / Axis 450 Outreach, with Sentinel validation and BEACON measurement.

## Decision

Preserve the approved controls and ordered sequence. **CL-004 remains the only active copy test.** CL-005 and CL-008 remain queued, not concurrent; CL-006 and CL-007 remain backlog. Do not change copy/winners.json.

No copy winner is promoted. The operational ceiling remains **450 confirmed prospect-facing sends per Pacific day**, but it is not a target that overrides DNC, eligibility, provider capacity, test isolation or list quality. Today's provider quota response is a hard stop for the attempted batch, not evidence about copy.

Add two operating guardrails:

1. When Gmail returns a quota or rate-limit error, reconcile Sent before retrying, wait at least the provider-prescribed interval, resume with one connection only, and increase slowly. Never use another sender to evade the limit.
2. Follow-up benchmarks must report the eligible nonresponder denominator at each step. Shares of total replies or meetings do not estimate the incremental causal value of another touch.

## Axis evidence observed

Sources: the durable lead ledger at blob d3c4a705c1b26ffd9d4ed99543b6669180175fa2 and the October 9 07:02 Pacific run checkpoint.

- October 8 ledger: **21 confirmed Gmail Sent / 450** under the CL-004 operating sequence, including Blue Window Cleaning plus 20 later Washington records.
- October 8 verified outcomes: 2 clear STOP replies, 2 verified delivery failures, 0 positive replies, 0 qualified conversations, 0 confirmed bookings and $0 supported revenue.
- October 9 through the observed checkpoint: **1 confirmed Gmail Sent / 450**, Eatonville Heating & Cooling, message 1a120fbcedbf72cd; delivery beyond Gmail acceptance is unknown.
- The next attempted October 9 send returned Gmail HTTP 403 RATE_LIMIT_EXCEEDED. Immediate Sent reconciliation found no message to that recipient, so no exposure or retry was counted.
- October 9 inbox at review: 0 messages. Positive replies: 0 / 1 accepted send; bookings: 0 / 1; supported revenue: $0.
- Current CL-004-assigned window, October 8–9: **22 accepted exposures**, 0 positive replies / 22 accepted, 0 bookings / 22 accepted, 2 opt-outs / 22 accepted, and 2 verified failures / 22 accepted. This is an accepted-send denominator; delivery remains unknown for messages without a verified delivery event.
- The sample and outcome windows are immature. The two opt-outs are a safety signal to monitor, not a statistically stable rate or a copy verdict.
- No campaign lift, delivery rate or winner is claimed.

## Evidence review

| Area | Evidence reviewed | Assessment for Axis |
|---|---|---|
| Subject lines | Gong's 2025/2026 observational material says short, priority-grounded subjects and less buzzword-heavy language associate with better outcomes; open-rate findings remain vulnerable to proxy and security scanning. | Retains CL-007 as backlog only. Opens are diagnostic, never the selection endpoint. |
| Opening and problem framing | Gong reports on 28M+ cold emails that product pitching, generic AI language, buzzwords and unsupported ROI framing associate with lower reply or meeting outcomes. The public article does not document recipient-level randomization. | Supports CL-004's sourced business observation and the ban on invented problems. It does not justify removing the owner-required AI discovery question or declaring a winner. |
| Outcome framing and length | The same Gong analysis associates 3–4 sentences and 100 words or fewer with higher replies. A separate executive study reports 50–100 words, but its population is C-suite sales cycles rather than local independent businesses. | Retains concise plain text and CL-006 as an unproven length test. Do not import an executive benchmark as a local-business target. |
| Personalization | No new randomized evidence reviewed today shows that first-name, compliment or AI-generated personalization alone causes more qualified replies. | Keep one verifiable operational detail; no invented praise, pain or familiarity. |
| CTA | Gong's 304,174-email analysis classified a meeting booked within 10 days as success and found interest CTAs strongest in cold email. Gong's 2026 executive analysis favors a concrete value offer over an immediate meeting request. Both are observational and use populations unlike Axis. | Supports CL-005, still queued. Primary measurement remains positive reply and downstream booking/revenue, not the article's headline lift. |
| Follow-up | Belkins reports 7.5M+ 2025 emails: the initial step had a 0.59% per-step reply rate, later steps collectively produced 58.6% of replies, and step 3 produced 35.6% of email-sourced meetings. A separate Belkins page cites 8.4% for the first follow-up, 3.8% for the fifth, and more than 3x complaint/unsubscribe pressure after four or more follow-ups. Denominators and cohort definitions are not reconciled on the public pages. | Supports testing one genuinely useful follow-up, not adopting a 3–5-step sequence. CL-008 stays queued and randomized among eligible nonresponders only. |
| Objection handling | Gong call research associates successful handling with pausing and clarifying rather than immediate rebuttal, but it studies live sales conversations, not cold-email replies. | Preserve Axis rules: opt-out/not interested → suppress without rebuttal; timing → ask permission and date; price → verified scope plus one clarification; existing provider → acknowledge without criticizing. |
| Deliverability | Google's current sender guidance requires authentication, accurate headers, TLS and spam-rate control; it advises gradual volume increases, reducing volume on deferrals/bounces, and after a quota error waiting at least 10 minutes before a single-connection retry. | The October 9 no-retry reconciliation was correct. Provider capacity overrides the 450 ceiling. The body STOP line does not replace any applicable header-level unsubscribe requirement. |
| Benchmarks | Belkins' follow-up and deliverability reports are large observational vendor datasets, but rates change with denominator, step eligibility, reply classification, client mix and time window. | Every external rate must retain source, population, period, numerator, denominator and reply definition. No external benchmark becomes an Axis target. |

No consequential AI-automation, booking-site, local-acquisition or TikTok development reviewed today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable sourced detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain text from Bradley with truthful identity, approved offer, complete private-config footer and exact opt-out.

These are operating controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact versions. Hold sender, offer, eligibility, cadence and compliance constant except for the named variable. Deduplicate by business and recipient.

Primary outcome: positive replies within 14 days. Secondary outcomes: qualified conversations, confirmed bookings at 30 and 60 days, and supported revenue/contact at 60 and 90 days. Guardrails: opt-outs, complaints and verified failure classes. Track bookings independently of replies. Use delivered denominators only when delivery is verified; otherwise report accepted/Sent and label delivery unknown.

**Sample P:** after an Axis baseline exists, calculate per-version sample size for a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until then, 200–400 eligible recipients per version is only a feasibility pilot, never proof.

**Rule K:** keep only if the primary endpoint's 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to bookings, revenue, opt-outs, complaints or failures. Retire when the interval rules out that effect. Otherwise label inconclusive. Safety stops override sample completion.

## Ordered hypotheses

| Order / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Approved AI/automation-led question | Sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Qualified conversations; 30/60-day bookings; 60/90-day revenue/contact | P; current accepted n=22, delivery incomplete | K; immediate kill for fabricated, stale or unsupported relevance; provider/DNC stops override |
| 2 / CL-005 | Discovery question | Offer to share two concrete observations; booking link secondary in both | Positive replies / eligible recipients | Qualified conversations, bookings, revenue/contact | P after CL-004 endpoint | K; reject if reply lift lacks downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized eligible nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop on any human reply, opt-out, bounce, complaint or DNC match; do not generalize multi-step vendor claims |
| Backlog / CL-006 | Existing body length | 50–80 words, proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after prior endpoint | K; skip if control is already in range |
| Backlog / CL-007 | Existing truthful question subject | Truthful 1–4-word business-priority subject with no promotional number or buzzword; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after prior endpoint | K; never select on opens alone |

## Executable handoff

1. Record this file's date and verified blob SHA.
2. Reconcile paginated Axis Gmail Sent using the Pacific-day boundary, plus inbox, live DNC label, drafts, suppressions, failures, thread state and bookings.
3. Preserve all existing message IDs and sticky assignments. Do not convert today's ambiguous quota attempt into a send.
4. Continue CL-004 only when the active sender workflow verifies DNC, suppression, daily count, eligible inventory and provider capacity. Do not force volume toward 450.
5. Do not start CL-005 concurrently. CL-008 is due only for randomized eligible nonresponders after five business days and after a fresh DNC/thread check.
6. Keep every outbound message individually researched and distinct. A sourced observation may frame relevance; it may not assert an unobserved problem.
7. Use the private sender-address record at send time; never publish the address in this research file.
8. BEACON reports state × niche × arm × hypothesis with exact numerators, denominators, windows and reply classes. Separate positive, neutral, automated, negative and opt-out replies. Unknown delivery remains unknown.
9. January/Infoton remains excluded. PrimeTouch Auto, Precision Pro Wash, Edmonds Garage Door Co., Cole's Appliance Repair and all other DNC/suppressed identities remain no-send.
10. If Gmail returns a rate-limit or quota error, reconcile Sent, pause at least the provider-prescribed interval, retry only through the authorized sequential workflow, and stop again on failure.

## Copy-library decision

**No new copy finding qualifies as an approved winner.** Preserve the existing control library.

Add only these operational guardrails:

- Follow-up evidence must use the eligible nonresponder denominator for each step.
- Provider quota errors require Sent reconciliation and a paced single-connection recovery; the daily ceiling never authorizes bypass.
- External copy claims must retain population, period, numerator, denominator, reply definition and causal limitations.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 9, 2026

[1] Axis Washington Outreach Run, October 9, 2026: https://github.com/1oldguyinaz-glitch/Master-Promt/blob/main/axis-omni-commerce/outreach/runs/2026-10-09-0702-washington.md
[2] Axis durable lead ledger, retrieved October 9, 2026: https://github.com/1oldguyinaz-glitch/Master-Promt/blob/main/axis-omni-commerce/data/leads/2026-09-29-recovery-candidates-1829.csv
[3] Gong, "Does cold email even work any more? Here's what the data says," published July 24, 2025, modified May 27, 2026: https://www.gong.io/blog/does-cold-email-even-work-any-more-heres-what-the-data-says
[4] Gong, "Do execs really reply to cold email? Here's what the data says," published January 29, 2026: https://www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says
[5] Gong, "Surprising cold email CTA that increases meeting bookings," analysis of 304,174 emails, modified March 6, 2026: https://www.gong.io/blog/this-surprising-cold-email-cta-will-help-you-book-a-lot-more-meetings
[6] Gong, "Avoid this tempting cold email mistake at all costs," analysis of 132,552 emails, modified March 6, 2026: https://www.gong.io/blog/avoid-this-tempting-cold-email-mistake-at-all-costs
[7] Belkins, "Sales follow-up statistics in B2B: 2026 study," retrieved October 9, 2026: https://belkins.io/blog/sales-follow-up-statistics
[8] Belkins, "B2B sales outreach strategy for 2026," retrieved October 9, 2026: https://belkins.io/blog/sales-outreach-strategy
[9] Belkins, "What are B2B cold email deliverability rates? 2026 study," retrieved October 9, 2026: https://belkins.io/blog/email-deliverability-rates
[10] Google, "Email sender guidelines," retrieved October 9, 2026: https://support.google.com/mail/answer/81126

Historical briefs and evidence remain in Git history. No prospect email was sent by COPY LAB.
