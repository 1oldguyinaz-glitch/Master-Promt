# COPY LAB — Daily Sales-Copy Brief

Date: 2026-09-21
Status: RESEARCH COMPLETE; HYPOTHESES READY FOR TESTING; NO DEPLOYMENT CLAIMED

## Executive directive
Prioritize relevance and signal quality over copy tricks. For first-touch outreach, test a short priority/problem-led message against the current AI/automation-led control. Keep the booking link secondary; the primary CTA should be a low-friction offer or question. Axis campaign outcomes decide winners.

## Verified / stronger evidence
1. Reply-rate benchmarks vary materially by dataset. Apollo places broad 2026 B2B cold-email reply rates around 3–6%; Woodpecker's last-90-day platform benchmark reports a 1.5% median across 56,614 campaigns. Treat external benchmarks as context, not targets.
2. Gong's 2026 executive-outreach analysis reports 1–4-word subject lines performing best for opens, 50–100-word emails producing the strongest replies, and reply rates falling sharply above 100 words. It also reports that product/buzzword/AI-heavy and vague ROI framing underperform priority/problem-led copy for executives.
3. Gong recommends an offer of value rather than an immediate meeting request for executive cold email. This is strong enough to test for Axis, not strong enough to assume universal causality across local-service SMB owners.
4. Woodpecker's platform benchmark shows diminishing marginal replies across a sequence: in 4–6-email campaigns, median per-touch reply rate fell from 1.0% on email 1 to 0.9%, 0.6%, 0.5%, then 0.3% on emails 5–6. One follow-up remains empirically defensible; claims that 4–7 touches are universally optimal are weak.
5. Gmail says user-reported spam should stay below 0.1% and must not reach 0.3% or higher. Yahoo requires spam complaint rates below 0.3%; bulk senders also face authentication and unsubscribe requirements. Deliverability is therefore a hard experimental guardrail, not a secondary metric.
6. Open rate is noisy because of privacy/tracking effects. Axis should continue prioritizing positive replies, booked meetings per delivered email, and downstream revenue.

## Weak / conditional claims — do not promote to library winners
- '4–7 touches is optimal.' Evidence is platform/practitioner-specific and marginal response declines substantially by later touches.
- 'Personalization doubles replies.' Definitions of personalization and cohorts vary; test situational relevance against Axis controls.
- '50–100 words is universally optimal.' Strong Gong evidence exists for executives, but Axis targets local-service SMBs; external validity is unproven.
- 'Never mention AI.' Gong's executive data supports testing removal of AI-first framing, not a universal ban.
- Subject-line open-rate gains should not be treated as revenue gains.

## Test queue

### CL-004 — Priority/problem lead vs AI-first lead
Control: current AI/automation-led first-touch positioning.
Variant: one verifiable operational condition or likely priority; no AI mention in the opening; one concise relevance bridge.
Primary metric: positive_reply_rate.
Secondary metric: booked_meetings_per_delivered; negative/unsubscribe_rate; revenue_per_1000_delivered.
Sample requirement: minimum 200 delivered per arm before directional judgment; target 400+ per arm for a more stable estimate unless a guardrail trips first. Balance niche, geography, and agent arm.
Keep rule: retain as a candidate winner if positive replies improve by >=25% relative AND bookings/delivered do not deteriorate materially AND negative/unsubscribe rate does not increase by >0.5 percentage points.
Kill rule: stop early for a material complaint/unsubscribe spike; otherwise retire if the variant shows no positive-reply lift after target sample or loses on bookings/revenue.

### CL-005 — Value-offer CTA vs direct meeting CTA
Control: direct request for a 15-minute meeting.
Variant: low-friction value offer/question as primary CTA; booking link remains secondary fast path.
Primary metric: positive_reply_rate.
Secondary metric: booked_meetings_per_delivered; qualified_conversation_rate; revenue_per_1000_delivered.
Sample requirement: minimum 200 delivered per arm; target 400+ per arm, balanced by niche and copy arm.
Keep rule: positive replies improve >=20% relative with no material decline in booked meetings/delivered.
Kill rule: retire if conversation volume rises but meetings/delivered or downstream revenue materially falls.

### CL-006 — 50–100 words vs current length
Control: current production email length.
Variant: 50–100 words, 3–4 short sentences, one problem/outcome frame and one primary ask.
Primary metric: positive_reply_rate.
Secondary metric: booked_meetings_per_delivered; revenue_per_1000_delivered.
Sample requirement: minimum 200 delivered per arm; target 400+ per arm.
Keep rule: retain if positive replies improve or remain statistically/practically equivalent while bookings or revenue improve and negative replies do not rise.
Kill rule: retire if qualified replies or bookings materially decline.

### CL-007 — Short priority subject vs current subject
Control: current subject-line family.
Variant: 1–4 words tied to a verifiable business priority/problem; no clickbait.
Primary metric: positive_reply_rate, not open rate.
Secondary metric: booked_meetings_per_delivered; open rate diagnostic only.
Sample requirement: minimum 250 delivered per arm because subject effects on downstream outcomes are likely smaller.
Keep rule: retain only on downstream reply/booking lift, not an open-rate-only win.
Kill rule: retire if opens rise without positive-reply or booking improvement.

### CL-008 — One follow-up vs no follow-up
Control: first touch only for otherwise eligible nonresponders.
Variant: one concise follow-up adding a new reason/value angle; suppress immediately on reply/opt-out.
Primary metric: incremental_positive_replies_per_prospect.
Secondary metric: incremental_booked_meetings_per_prospect; negative/unsubscribe_rate; revenue_per_prospect.
Sample requirement: 250 eligible prospects per arm minimum.
Keep rule: incremental positive replies/bookings justify the extra send without a material complaint/unsubscribe increase.
Kill rule: incremental business yield is negligible or suppression/deliverability guardrails worsen.

## Copy-library candidate
CANDIDATE — not yet a proven winner:
Priority/problem -> relevance/proof -> value offer/question -> secondary booking path.

First-touch constraints to test: 50–100 words; one primary CTA; no unsupported ROI; no fake personalization; no AI-first opener unless the control requires it; every observation must be verifiable.

Do not promote this candidate to `copy/winners.json` until Axis campaign data satisfies the keep rule.

## Deliverability guardrails
- Suppress opt-outs immediately.
- Track delivered, bounced, positive, negative, unsubscribe/complaint, booked, held, paid, and revenue separately.
- Diagnose deliverability/list quality before blaming copy when reply rates collapse.
- Gmail: target user-reported spam <0.1%; never allow >=0.3%.
- Yahoo: keep complaint rate <0.3%; follow authentication and applicable unsubscribe requirements.

## Sources reviewed 2026-09-21
- Gong, 'Do execs really reply to cold email?' (published Jan. 29, 2026; modified May 27, 2026).
- Gong, cold-email / ROI research (132,000-email analysis; ROI language associated with 15% lower success in that dataset).
- Apollo, 2026 cold-outreach reply-rate and personalization benchmarks.
- Woodpecker cold-email benchmarks, updated Aug. 5, 2026: median reply rate 1.5% across 56,614 campaigns; sequence-level delivered-email samples reported by touch.
- Google Gmail Email Sender Guidelines FAQ, current 2026 guidance.
- Yahoo Sender Hub Best Practices / FAQs, current 2026 guidance.

## Runtime instruction
COPY LAB -> VERITY -> DIRECTOR -> AXIS -> BEACON -> AXIS OMNI.
External evidence creates hypotheses. Axis data creates winners. Do not claim deployment without a verified execution result.