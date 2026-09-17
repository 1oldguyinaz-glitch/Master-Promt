# AXIS OMNI — Prelaunch Dashboard

> Status: **PRE-PAYMENT / DRAFT-ONLY**
>
> Nothing on this page is a live product listing. This dashboard is for reviewing the system before Shopify Collective is activated.

---

## Current system state

| Component | Status | Notes |
|---|---|---|
| AXIS OMNI orchestrator | READY | Runtime and state flow created |
| AXIS execution layer | READY FOR DRAFT WORK | Live writes remain gated |
| VERITY validation layer | READY | Authorization, economics, and risk gates defined |
| BEACON intelligence layer | READY | Historical signal store loaded |
| DIRECTOR creative layer | READY | Waits for approved product data |
| SQLite state + audit log | READY | Tracks runs and decisions |
| Supplier connector interface | READY | Waiting for real supplier network |
| Shopify connector | DRAFT-ONLY | No live publishing |
| Shopify Collective | BLOCKED BY PLAN/ELIGIBILITY | Activate after paid plan |
| Paid ads | OFF | Not allowed before proof loop |
| Live products | 0 | Correct for current stage |

---

## BEACON starting signal profile

Historical TikTok/web research is used as a **prior**, not proof.

Priority product characteristics:

- Automotive / driver convenience
- Cleaning / utility
- Organization / storage
- Obvious problem → solution
- Visually demonstrable in about 15–20 seconds
- Low sizing complexity
- Low return risk
- Low claim burden
- Easy to explain in one short-form video

Historical evidence can increase search priority, but every candidate still requires fresh demand, supplier authorization, fulfillment, and margin validation.

---

## First supplier search profile

AXIS should search authorized supplier catalogs for:

1. Automotive convenience accessories
2. Driver organization products
3. Car cleaning / detailing utility products
4. Household utility products
5. Compact organization / storage products

Preferred supplier properties:

- Already selling finished products
- Reseller / retailer authorization
- Direct fulfillment
- Live inventory or reliable stock data
- Tracking synchronization
- Defined returns
- No required bulk inventory purchase
- Acceptable retailer margin
- Shopify-compatible integration where possible

---

## Product eligibility gate

A product enters BEACON ranking only when:

```text
Authorized to resell
+ Active inventory
+ Supplier can fulfill
+ Tracking supported
+ Returns defined
+ Platform rules allow it
+ Landed costs can be calculated
+ Positive contribution margin
= ELIGIBLE PRODUCT
```

---

## AXIS OMNI live flow

```text
Supplier Catalogs
      ↓
AXIS imports authorized products
      ↓
BEACON applies historical priors + fresh demand data
      ↓
Top 10 existing products ranked
      ↓
VERITY checks authorization + economics + risk
      ↓
DIRECTOR creates offer / listing / creative
      ↓
VERITY final claims check
      ↓
AXIS creates Shopify DRAFT
      ↓
Human review
      ↓
Publish approval
      ↓
Customer order
      ↓
Supplier fulfillment
      ↓
Tracking sync
      ↓
Financial waterfall
      ↓
BEACON measures actual contribution profit
      ↓
Next product cycle
```

---

## Financial waterfall

```text
Customer payment
→ Platform / processing obligations
→ Taxes and required reserves
→ Supplier product cost
→ Shipping / fulfillment
→ Refund / chargeback reserve
→ Contribution profit
→ Reinvestment or owner distribution
```

Revenue is never treated as profit.

---

## First proof target

AXIS OMNI is not considered proven until it completes:

```text
1 authorized supplier
→ 1 real product
→ 1 Shopify draft
→ 1 approved live listing
→ 1 real order
→ supplier fulfillment
→ tracking received
→ delivery confirmed
→ actual contribution profit calculated
→ next product recommendation produced
```

---

## Current blocker

The remaining live-platform blocker is Shopify Collective eligibility / paid Shopify activation.

Until that gate is opened, AXIS OMNI remains intentionally in **draft-only mode**.

---

## What happens immediately after activation

1. Confirm Shopify Payments / Collective eligibility.
2. Open supplier discovery.
3. Search the priority categories above.
4. Collect real supplier and product economics.
5. Run VERITY.
6. Have BEACON rank the Top 10.
7. Import exactly one approved product as a Shopify draft.
8. Review the transaction waterfall before publishing.

---

**Operating rule:** do not fabricate supplier authorization, product data, demand, margin, reviews, inventory, or fulfillment status to make the system appear further along than it is.
