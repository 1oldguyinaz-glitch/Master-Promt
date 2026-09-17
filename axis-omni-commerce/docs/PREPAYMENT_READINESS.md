# AXIS OMNI — Pre-Payment Readiness Status

## Current state

The connected Shopify store is on a trial plan and contains no products. AXIS OMNI is therefore operating in pre-payment, draft-only mode.

Completed before any Shopify monthly payment:

- AXIS OMNI runtime state model
- SQLite persistence and audit-event tables
- deterministic policy engine
- AXIS / VERITY / BEACON routing core
- agent registry
- common commerce connector interface
- draft-only Shopify connector boundary
- BEACON historical-signal seed data
- BEACON historical-signal persistence loader
- first supplier-search profile focused on automotive, driver convenience, cleaning/utility, and organization products
- GitHub Actions smoke-test workflow
- live-publish approval gate
- supplier authorization and margin gates

## Paid/eligibility boundary

Shopify Collective is the preferred first supplier network because it supports authorized supplier discovery, catalog import, automatic order routing, inventory/price synchronization, supplier fulfillment, and supplier payment after fulfillment for eligible stores.

The next platform gate is Shopify Collective eligibility, which requires an active Shopify plan and other Shopify eligibility conditions. Do not fabricate products or supplier authorization to bypass this gate.

## Immediately after plan activation

1. Confirm Shopify Payments and Collective eligibility.
2. Open Collective Discovery.
3. Search the priority categories in `config/first_supplier_search_v1.json`.
4. Prefer Instant Import suppliers with verified tracking and acceptable retailer margins.
5. Export or record the top candidate supplier/product data.
6. Run VERITY authorization, economics, fulfillment, returns, and policy checks.
7. Have BEACON rank the eligible products using fresh evidence plus historical priors.
8. Import exactly one approved product as a Shopify draft.
9. Review the full supplier-first transaction waterfall before live publication.

## Do not do yet

- pay for inventory
- enable paid advertising
- publish an unverified product
- invent supplier permission
- treat historical TikTok signals as proof of current demand
- connect Amazon or TikTok Shop before the Shopify proof loop works
