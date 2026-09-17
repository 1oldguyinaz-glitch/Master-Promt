# BEACON Historical Signal Store

## Purpose

Preserve validated historical product, audience, creative, supplier, and channel signals so AXIS OMNI does not restart product research from zero on every cycle.

This is a BEACON subsystem, not a separate agent.

## Required behavior

At the beginning of every opportunity-ranking cycle:

1. Load the historical signal store.
2. Separate observations from hypotheses and estimates.
3. Apply historical evidence only as a prior weighting signal.
4. Retrieve fresh current-market evidence for each candidate.
5. Increase confidence only when fresh evidence agrees with the historical signal.
6. Decrease or reverse the historical weighting when newer evidence contradicts it.
7. Never treat past engagement, audience demographics, or a prior trend as proof of present demand.
8. Record the final outcome after each experiment so the signal store compounds over time.

## Signal classes

Store at minimum:

- product attributes;
- category;
- customer segment;
- platform;
- creative pattern;
- supplier;
- retail price;
- contribution margin;
- traffic source;
- conversion rate;
- return/refund rate;
- fulfillment performance;
- sample size;
- observation period;
- confidence;
- actual result;
- invalidating evidence.

## Bayesian operating rule

Historical evidence establishes a prior, not a conclusion.

For each candidate, BEACON must conceptually update:

```text
historical prior
+ current supplier evidence
+ current demand evidence
+ current economics
+ current platform evidence
= updated opportunity assessment
```

The system should prefer candidates whose current evidence reinforces historically productive attributes, while preserving exploration for new categories.

## Exploration requirement

Do not allow the historical store to create a self-reinforcing filter bubble.

For every Top Ten list:

- up to 8 candidates may exploit existing positive signals;
- at least 2 candidates should test credible adjacent or novel hypotheses when sufficient evidence exists.

This is a default research rule, not a requirement to launch weak products.

## Current seed profile

Load `data/historical_signals/tiktok_web_trends.seed.json` as the initial seed.

Current priority characteristics include:

- automotive and driver convenience;
- cleaning and utility;
- organization and storage;
- visually demonstrable products;
- clear problem/solution products;
- low sizing complexity;
- low return risk;
- products whose value is visible quickly in short-form video.

## Output additions

Every BEACON product-ranking output must include:

- `historical_signal_match`: 0-100;
- `historical_signal_reasons`;
- `fresh_evidence_strength`: 0-100;
- `historical_fresh_conflict`: true/false;
- `exploit_or_explore`: `EXPLOIT` or `EXPLORE`;
- `updated_confidence`;
- `next_learning_value`.

Historical signal matching must never override VERITY authorization, compliance, or unit-economics gates.
