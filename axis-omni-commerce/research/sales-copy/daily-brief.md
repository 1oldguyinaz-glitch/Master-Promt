# COPY LAB — Daily Sales-Copy Brief
Date: 2026-10-08 (Pacific)
Status: VERIFIED REPOSITORY HANDOFF; NEW HYPOTHESES UNPROVEN
Next owner: Axis Washington Business Hours / Axis 450 Outreach, with Sentinel validation and BEACON measurement.

## Decision

Preserve the approved controls and sequence. **CL-004 remains the only active copy test.** CL-005 and CL-008 remain queued, not concurrent; CL-006 and CL-007 remain backlog. Do not change `copy/winners.json`.

The first five-recipient verification pilot is complete: four confirmed Gmail Sent records on October 7 plus one CL-004 exposure on October 8. Do not infer delivery, lift or a winner from Gmail acceptance. The operational ceiling remains **450 confirmed prospect-facing sends per Pacific day**, subject to stricter active test gates, eligible inventory and provider capacity.

Add one measurement rule: every external benchmark must retain its original denominator, time period, reply definition and source. Do not copy a rate from a derivative roundup when the primary report uses a different denominator.

## Axis evidence observed

- Latest checkpoint: `axis-omni-commerce/outreach/runs/2026-10-08-0700-washington.md`.
- October 8: **1 confirmed Gmail Sent / 450**; message `1a11bd07d5e2f86c`, Blue Window Cleaning, WA × window_cleaning × STAN.
- CL-004 verified exposures: **1**. Gmail accepted the message at 07:00:10 PT. Downstream delivery is unknown.
- Positive replies: 0 / 1 accepted send. Qualified conversations: 0 / 1. Confirmed bookings: 0 / 1. Supported revenue: $0. The outcome window is immature.
- Four October 7 sends remain preserved as prior-day records and do not count against October 8.
- No new inbox message was present at this review. PrimeTouch Auto remains hard-bounce suppressed; January/Infoton remains excluded.
- No winner, delivery claim or campaign lift is claimed.

## Evidence review

### Strong operational findings

1. **Denominators change the story.** Belkins’ June 26, 2026 report analyzed 7,530,489 cold emails sent in 2025 and reports 34,393 unique replies, excluding autoreplies and bounces: **0.45% replies per email sent**. Belkins explicitly says earlier reports divided replies by unique openers and therefore produced much higher-looking rates. Open tracking was disabled in the 2025 dataset. [1]
2. **Derivative benchmark summaries can be materially wrong for the current study.** A Prospeo guide retrieved October 8 attributes a 5.8% average reply rate and 16.5M-email analysis to Belkins, while the linked current Belkins report documents 7.53M emails and 0.45% replies per send. The Prospeo page also mixes vendor datasets, internal tests, Reddit anecdotes and open-rate findings. Treat it as practitioner opinion, not an Axis target. [2]
3. **Targeting fit may outweigh title prestige.** In the same Belkins observational dataset, owners/founders and very small companies had higher reply rates than large-company executives and enterprises. This aligns with Axis’s local independent-business focus, but it is not causal evidence for copy selection. [1]
4. **Deliverability and identity remain prerequisites.** Google requires authentication, TLS, RFC 5322 formatting and spam rates below 0.3% for mail to personal Gmail accounts. High-volume marketing traffic has additional one-click-unsubscribe requirements. The required body STOP line and physical address do not replace applicable header-level requirements. [3]
5. **Open rate remains diagnostic only.** The 5.5M-email Belkins/Reply.io subject-line study reports open and reply associations for personalization, questions and length, but it does not establish recipient-level randomization and relies heavily on unreliable open data. It can motivate CL-007 only; it cannot select a winner. [4]

### Retained practitioner hypotheses

- A sourced operational observation may earn more positive replies than an AI-led general opener: CL-004.
- A concrete value offer may outperform a discovery-only CTA: CL-005.
- One useful follow-up may recover qualified conversations from nonresponders: CL-008.
- A short truthful priority subject may outperform the current truthful subject on downstream outcomes: CL-007, backlog.
- Morning-send observations from Belkins are not a timing winner for Axis because campaign composition and recipient time zones were not randomized.

### Weak or rejected claims

- Universal “best” subject length, send day, send hour, word count, follow-up count or fixed lift.
- Open-rate optimization as a campaign objective.
- Dashboard reply rates that combine human, automated, neutral, negative and opt-out responses.
- Any benchmark copied without its original denominator and reply definition.
- Any claim that one accepted Axis email validates CL-004.

No consequential AI-automation, booking-site, local-acquisition or TikTok development reviewed today changes the approved Axis offer.

## Preserved controls

- **CL-001:** one verifiable sourced detail; no invented problem, familiarity or compliment.
- **CL-002:** one clear primary question; booking link secondary.
- **CL-003:** concise plain text from Bradley with truthful identity, approved offer, complete private-config footer and exact opt-out.

These are operating controls, not proven winners.

## Common test design

Randomize by business and stratify by state × niche × sticky arm. Freeze exact versions. Hold sender, offer, eligibility, subject, cadence and compliance constant except for the named variable. Deduplicate by business and recipient.

Primary outcome: positive replies within 14 days. Secondary outcomes: qualified conversations, confirmed bookings at 30 and 60 days, and supported revenue/contact at 60 and 90 days. Guardrails: opt-outs, complaints and verified failure classes. Track bookings independently of replies. Use delivered denominators only when delivery is verified; otherwise report accepted/Sent and label delivery unknown.

**Sample P:** after an Axis baseline exists, calculate per-version sample size for a preregistered worthwhile absolute lift using two-sided alpha 0.05 and 80% power. Until then, 200–400 eligible recipients per version is only a feasibility pilot.

**Rule K:** keep only if the primary endpoint’s 95% interval excludes zero and reaches the preregistered worthwhile effect, with no material harm to bookings, revenue, opt-outs, complaints or failures. Retire when the interval rules out that effect. Otherwise label inconclusive. Safety stops override sample completion.

## Ordered hypotheses

| Order / ID | Control | Unproven variant | Primary metric | Secondary metric | Sample | Kill / keep |
|---|---|---|---|---|---|---|
| 1 / CL-004 | Approved AI/automation-led question | Sourced operational observation → possible relevant outcome; never assert an unobserved problem | Positive replies / eligible first-touch recipients | Qualified conversations; 30/60-day bookings; 60/90-day revenue/contact | P; current n=1 accepted, delivery unknown | K; immediate kill for fabricated, stale or unsupported relevance |
| 2 / CL-005 | Discovery question | Offer to share two concrete observations; booking link secondary in both | Positive replies / eligible recipients | Qualified conversations, bookings, revenue/contact | P after CL-004 endpoint | K; reject if reply lift lacks downstream quality |
| 3 / CL-008 | No follow-up | One genuinely useful follow-up after five business days to randomized eligible nonresponders | Incremental positive replies / randomized nonresponders | Incremental bookings, revenue/prospect, opt-outs, complaints | P from observed nonresponder baseline | K; stop on any human reply, opt-out, bounce or complaint |
| Backlog / CL-006 | Existing body length | 50–80 words, proposition and CTA fixed | Positive replies / recipients | Bookings, revenue/contact, opt-outs | P after prior endpoint | K; skip if control is already in range |
| Backlog / CL-007 | Existing truthful subject | Truthful short priority subject; body fixed | Positive replies / recipients | Bookings and revenue/contact; opens diagnostic only | P after prior endpoint | K; never select on opens alone |

## Executable handoff

1. Record this file’s date and blob SHA.
2. Reconcile paginated Axis Gmail Sent using the Pacific-day boundary, plus inbox, drafts, suppressions, failures, thread state and bookings.
3. Preserve the five confirmed pilot message IDs. Do not send beyond the active repository test gate merely because the daily ceiling is 450.
4. Continue CL-004 only after the active configuration authorizes a larger randomized cohort. Persist lead ID, arm, exact version, Gmail ID, acceptance state and any verified delivery event.
5. Do not start CL-005 concurrently. CL-008 is not due until an eligible nonresponder reaches five business days.
6. Use the private sender-address record at send time; never publish the address in this research file.
7. Process objections: opt-out/not interested → suppress without rebuttal; timing → obtain permission and date; price → use verified scope/pricing plus one clarification; existing provider → acknowledge without inventing deficiencies.
8. BEACON reports state × niche × arm × hypothesis with exact numerators, denominators, windows and reply classes. Unknown delivery remains unknown.
9. January/Infoton remains excluded. PrimeTouch Auto remains no-retry suppressed.

## Copy-library decision

**No new copy finding qualifies as an approved winner.** Preserve the existing control library. Add only the benchmark-integrity guardrail: record source, population, period, denominator and reply classification before using any external rate.

Required booking path:
https://cal.com/bradley-dennis-ddfihy/15min?overlayCalendar=true

Required opt-out:
Reply STOP to unsubscribe.

## Sources checked October 8, 2026

[1] Belkins, “What are B2B cold email response rates? Belkins’ 2026 study,” updated June 26, 2026: https://belkins.io/blog/cold-email-response-rates  
[2] Prospeo, “Best Cold Email Templates That Get Replies (2026),” retrieved October 8, 2026: https://prospeo.io/s/best-cold-email-templates  
[3] Google, “Email sender guidelines,” retrieved October 8, 2026: https://support.google.com/mail/answer/81126  
[4] Belkins, “How different B2B cold email subject lines perform: Belkins’ 2025 study,” published August 6, 2025: https://belkins.io/blog/b2b-cold-email-subject-line-statistics

Historical briefs and evidence remain in Git history. Latest persisted Axis outcome read: `axis-omni-commerce/outreach/runs/2026-10-08-0700-washington.md`.
