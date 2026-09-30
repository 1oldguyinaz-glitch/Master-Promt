# COPY LAB — Daily Sales-Copy Brief
Date: 2026-09-29 (Pacific)
Status: RESEARCH AND HANDOFF; ALL NEW TESTS UNPROVEN
Next owner: Axis 450 Outreach, including Sentinel checks and BEACON measurement.

## Decision
Preserve the existing control. Test ONE copy variable at a time. Do not promote winners from 200–400 emails per version. The daily ceiling is 450 prospect-facing sends including replies and follow-ups, subject to lower provider capacity. This brief does not prove sending recovery.

## Verified external findings and limitations
- Woodpecker's benchmark, updated August 5, 2026, uses the last 90 days of **2025**, not a live trailing period. Its headline reply median is 1.5% across 56,614 campaigns; this is total replies, not positive replies or bookings. Observational platform data are context, not Axis forecasts. Its sequence data show declining later-touch replies in longer sequences; that does not establish the causal value of adding touches. [1]
- Gong's January 29, 2026 executive analysis associates short subjects with opens and concise messages with replies, favors relevant priorities over buzzwords, and recommends a concrete value offer. These are vendor observations about executives, not randomized evidence for local business owners. Treat short subjects, relevant openings and value offers as test candidates, not universal rules. [2]
- Google advises truthful sender/subject information, gradual volume increases, reducing volume when bounces/deferrals occur, and Postmaster spam rates below 0.1%, avoiding 0.3% or higher. It discourages unsolicited messages to people who did not sign up. A 450/day internal ceiling is not a deliverability guarantee or exemption from provider rules. Gmail does not verify third-party open rates. [3]
- Woodpecker's two-version calculator illustrates the sample-size problem: at a 1.5% reply baseline, detecting a 50% relative increase requires about 4,414 observations per version under its 95%-confidence/80%-power assumptions. Its positive-reply baseline defaults are estimates, not measurements of Axis. [4]

## Axis evidence
Read existing September 20 run report: it records nine sends with sticky arms and zero human replies at that snapshot; bookings and revenue were not independently queried. That record lacks message IDs and is not a validated winning experiment. Repository searches did not surface newer outcome reports in the inspected runs directory. No current conversion baseline has been established. Preserve all historical logs and assignments.

## Controls and test queue
Preserve CL-001 situational relevance, CL-002 discovery CTA with secondary booking link, and CL-003 concise copy as existing recorded controls—not proven winners. Preserve CL-004 through CL-008 from September 21; their prior small-sample winner thresholds are superseded by the plan below. Defer all but CL-004 until its preregistered evaluation finishes.

Common design for each test: randomize by business, stratify by state/niche and sticky agent arm, keep eligibility, pricing and cadence identical. Deduplicate businesses. One primary outcome and one comparison at a time. Freeze actual control text/version before sending. Use a 14-day response window after assignment, 30 days for booking and 60 days for revenue. Do not count autoreplies or opt-outs as positive replies. If delivery is not known, label denominator accepted/sent, never delivered. Report numerator, denominator and 95% interval.

Sample requirement P: calculate before launch from Axis positive-reply baseline, desired absolute lift, two-sided alpha 0.05 and 80% power. Until baseline exists, 200–400 per version is a feasibility pilot only. As planning context, [4] gives about 13,391 per version for 0.5% to 0.75% positive replies; this can take months under the daily cap. Do not split this volume across five simultaneous experiments. A scarce reply dataset can remain inconclusive.

Common decision K: keep as a candidate only at the planned endpoint if the primary difference's 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material booking/revenue or opt-out harm. If the interval rules out the worthwhile effect, retire; otherwise mark inconclusive and retain control. Safety stops do not require completing the sample. No significance claim from daily peeking, no equivalence claim from a nonsignificant result.

| ID | Control → variant (hypothesis) | Primary | Secondary | Sample and decision |
|---|---|---|---|---|
| CL-004 | Existing AI/automation-led opening → one sourced operational observation and relevant possible outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Bookings / delivered when known; qualified conversations; revenue/contact; opt-outs | P; K; worthwhile effect fixed before launch |
| CL-005 | Existing discovery question → concrete offer to share two useful observations; booking link secondary in both | Positive replies / recipients | Bookings, qualified conversations, revenue/contact, opt-outs | P; K; reject if extra replies do not improve downstream quality |
| CL-006 | Actual existing body length → 50–100 words, holding proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P; K; if control already matches, skip redundant test |
| CL-007 | Actual existing subject → truthful 1–4-word priority subject, body unchanged | Positive replies / recipients | Bookings, revenue/contact; opens diagnostic only | P; K; never select on opens alone |
| CL-008 | No follow-up → one useful follow-up after five business days to eligible nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, extra sends | P using nonresponder baseline; K; five-day spacing is an operational hypothesis, not proven optimum |

## Executable sequence and objection handling
Day zero: sender Bradley; one sourced relevance point, a possible useful outcome without quantified promises, one primary CTA, the existing secondary 15-minute booking URL and exact opt-out line. Use existing control outside the single active test.
Follow-up: only if due under an approved sequence or CL-008 assignment; add a concrete new observation, not repeated pressure. Stop follow-ups on any human reply and classify it.
Objections: opt-out/not interested → suppress, no rebuttal. Timing objection → acknowledge and obtain permission for a later date. Price question → answer only with verified scope/pricing, then one clarification. Existing provider → acknowledge; do not invent deficiencies. These are proposed operational practices, not measured conversion improvements.

## Copy library
Add only as UNPROVEN CANDIDATE: sourced observation → possible useful outcome → concrete value offer → secondary booking path. Never fabricate case studies, savings, prior familiarity or AI capabilities. Existing requirement remains:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true
Reply STOP to unsubscribe.
Do not modify copy/winners.json without Axis evidence.

## Sender handoff and guardrails
Read this file's date/version before copy generation. Reconcile Sent and durable history; immediately suppress STOP businesses across sender identities. Quarantine DNS failures, full inboxes and rejections; do not retry while Gmail retries. Preserve January exclusion. Process sequential batches of 15–25 with count/suppression rechecks. Provider limits, missing verified sender details or unknown suppression state block sending, not independent research. Persist confirmed Gmail IDs and copy/test version. Carry forward all historical leads, assignments and records. Report zero, unknown and not queried distinctly.
No consequential new AI/TikTok offer change was validated in this review. Today is Tuesday; no Monday supplement is due.

## Sources (checked September 29, 2026)
[1] https://woodpecker.co/cold-email-benchmarks/ — updated 2026-08-05; period explicitly last 90 days of 2025.
[2] https://dev.www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says — published 2026-01-29; search-indexed source reviewed.
[3] https://support.google.com/mail/answer/81126 — official sender guidance, retrieved today.
[4] https://woodpecker.co/cold-email-ab-test-calculator/ — planning table reviewed today; illustrative assumptions.
Prior controls/history: September 21 version of this file remains in Git history; axis-omni-commerce/outreach/runs/2026-09-20-1214.md.
