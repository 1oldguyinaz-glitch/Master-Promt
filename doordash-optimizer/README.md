# DoorDash Optimizer

Purpose: preserve the best-performing DoorDash decision system so future shifts can be run against one stable benchmark instead of changing rules mid-shift.

## Benchmark day

**September 13, 2026** is the current benchmark because it produced the strongest confirmed time efficiency:

- Gross earnings: **$172.97**
- Dash time: **6h 11m**
- Active time: **5h 27m**
- Completed deliveries: **13**
- Accepted offers: **9**
- Gross per Dash hour: **$27.97/hr**
- Gross per active hour: **$31.74/hr**

## Primary objective

Maximize **gross dollars per total Dash hour** while controlling mileage, wait risk, and bad repositioning.

### Decision hierarchy

1. Expected dollars per hour
2. Expected completion time
3. Displayed payout
4. Direction / quality of destination zone
5. Dollars per mile
6. Item count / wait risk

Mileage is an operating-cost metric, not an automatic veto when the expected hourly return is strong.

## Live offer protocol

During a shift, the driver provides the useful offer data available on screen, normally payout, shown mileage, merchant/order type, stack status, and direction when relevant.

The assistant responds **YES — ACCEPT** or **NO — DECLINE** first, immediately. Explanation is only added when requested or when the decision is genuinely borderline.

Fuel range is tracked for logistics only and is **not** an acceptance/decline variable.

## Working thresholds derived from the benchmark system

These are heuristics, not hard guarantees:

- Prefer offers projecting **$28+/hour**.
- Offers projecting roughly **$22–$24/hour or less** are usually declines unless they create unusually valuable paid repositioning.
- Short restaurant offers around **$7.50+** can be attractive when pickup/drop-off is fast.
- Stacked offers around **$11+** can be attractive when total time and route geometry remain efficient.
- Grocery/retail orders around **$8.50–$9+** can work when item count is low and shopping time is short.
- High-payout orders can override a weak dollars-per-mile ratio when expected completion time still creates a strong hourly rate.
- Avoid slow merchants, oversized shop orders with weak payout, and destinations that strand the driver in low-demand areas unless compensation is sufficient.

## Current comparison set

| Date | Gross | Active time | Dash time | Deliveries | Gross / active hr | Gross / Dash hr | Miles | Gross / mile |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Sep 13, 2026 | $172.97 | 5h 27m | 6h 11m | 13 | $31.74 | $27.97 | — | — |
| Sep 14, 2026 | $153.97* | 5h 41m | 7h 27m | 13 | $27.09 | $20.67 | 114 | $1.35 |
| Sep 15, 2026 | $167.17 | 6h 44m | 9h 04m | 18 | $24.83 | $18.44 | 120 | $1.39 |

\* Sep 14 gross includes a $20 cash tip.

## Measurement rule

At end of shift record:

- DoorDash app gross
- Cash tips separately
- Active time
- Dash time
- Completed deliveries
- Accepted offers
- Start odometer
- End odometer
- Total vehicle miles
- Gross / active hour
- Gross / Dash hour
- Gross / vehicle mile

Update the benchmark only when a new day clearly beats the current benchmark on the primary metric without creating obviously worse operating economics.

## Important assumption discipline

Do **not** assume DoorDash changes future offers because of which offers were accepted or declined unless supported by actual evidence. Treat that as a hypothesis to test, not a rule.
