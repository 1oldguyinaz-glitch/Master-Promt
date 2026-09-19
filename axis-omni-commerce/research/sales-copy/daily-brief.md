# COPY LAB — Daily Sales-Copy Brief

Date: 2026-09-19
Status: VERIFIED RESEARCH COMPLETE; TEAM BRIEF ISSUED

## Executive directive
The next copy cycle should optimize for relevance, brevity, and lower-friction CTAs before increasing message complexity. External research is treated as hypothesis input only; Axis campaign data decides winners.

## Verified findings
1. Broad B2B cold-email reply rates in 2026 are commonly around 3–6%; sub-3% performance can indicate targeting or deliverability problems, while stronger campaigns can exceed that with tighter segmentation and relevance.
2. Situational relevance (why this prospect, why now) is stronger than shallow personalization such as generic compliments or name-dropping.
3. Short, focused emails generally outperform long, feature-heavy messages; one clear CTA is preferable to multiple competing asks.
4. Deliverability is a first-order constraint. Weak inbox placement can make good copy look bad, so copy results must be interpreted alongside delivery and suppression data.
5. Positive-reply rate, booked-meetings-per-delivered, and downstream revenue are more useful decision metrics than open rate alone.

## Team brief
### STAN
Lead with a concrete observation or situational reason for contact. Ask one discovery-oriented question. Do not front-load feature lists.

### CUSTOMER_SERVICE
Keep the listener-first style, but tighten first-touch copy. One acknowledgement + one relevant question + one easy next step.

### BRIDGE
Preserve warmth, but remove generic compliments and fake familiarity. Relevance must be specific and provable.

### SENTINEL
Protect deliverability and suppression rules. Track delivered, bounced, replied, positive, negative/unsubscribe, booked, and revenue states separately. Do not treat opt-outs as future targets.

### VERITY
Reject unsupported claims, vague ROI promises, fake personalization, and any message that implies knowledge we do not actually have.

### BEACON
Judge experiments on positive reply rate, qualified-conversation rate, booked meetings per delivered email, and revenue per 1,000 delivered. Open rate is diagnostic only.

## Test queue
### CL-001 — Situational relevance vs generic AI pitch
Control: current generic AI/automation positioning.
Variant: one concrete observed business condition + one discovery question.
Primary metric: positive_reply_rate.
Secondary metric: booked_meetings_per_delivered.
Sample requirement: balanced test across comparable fresh prospects before declaring a winner.
Keep rule: retain only if the variant materially improves positive replies without increasing negative/unsubscribe rate.
Kill rule: retire if no meaningful lift or if negative replies increase.

### CL-002 — Discovery CTA vs immediate meeting ask
Control: direct meeting-oriented CTA.
Variant: low-friction interest/discovery question with booking link retained as a secondary fast path.
Primary metric: positive_reply_rate.
Secondary metric: qualified_conversation_rate and booked_meetings_per_delivered.
Keep rule: retain if it creates more qualified conversations and does not reduce bookings per delivered.
Kill rule: retire if conversation volume rises but downstream booking quality falls materially.

### CL-003 — Short copy vs long feature-heavy copy
Control: current longer feature/automation explanation.
Variant: concise message under roughly 120–150 words with one problem/outcome frame and one main ask.
Primary metric: positive_reply_rate.
Secondary metric: revenue_per_1000_delivered.
Keep rule: retain if concise copy improves or matches positive replies while reducing negative response rate.
Kill rule: retire if brevity removes necessary context and qualified responses fall.

## Messaging frame to test
Observation -> relevance -> question -> secondary booking path

Example structure:
"Noticed [specific, verifiable condition]. We help local service businesses remove manual follow-up and booking friction, but the useful part depends on where your bottleneck actually is. How are you handling [specific process] today? If it's easier, here's the 15-minute link."

## Sources reviewed
- Apollo, 2026 cold-outreach reply-rate benchmarks.
- Apollo, 2026 personalization research: situational relevance, shorter emails, and trigger-based outreach.
- Apollo, 2026 sequence-rewrite guidance: diagnose deliverability, segment, relevance, value, and CTA before rewriting.
- Gong, 2026 executive cold-email research: long, product-heavy, priority-disconnected messages underperform with executives.
- Apollo/Tolly 2026 GTM effectiveness report for email-to-meeting context.

## Runtime instruction
COPY LAB -> VERITY -> DIRECTOR -> AXIS -> BEACON -> AXIS OMNI.
Do not auto-promote any external best practice into a winner. Test it against Axis data, retain proven variants, and retire weak variants.
