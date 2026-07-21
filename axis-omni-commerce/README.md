# AXIS OMNI

**Autonomous Commerce Implementation System**

AXIS OMNI is a modular prompt-and-workflow repository for connecting to suppliers that already sell finished products, identifying authorized products worth distributing, validating true unit economics, creating compliant offers and listings, routing orders to suppliers, and using real performance data to determine what to sell next.

This repository packages the finalized operating system into a GitHub-ready structure.

## Core operating loop

```text
Supplier catalogs
→ Eligibility and authorization
→ Top-ten opportunity ranking
→ Market and margin validation
→ Platform routing
→ Offer and listing production
→ Deployment
→ Supplier fulfillment
→ Financial waterfall
→ Analytics and optimization
→ Next product cycle
```

## Operating hierarchy

| Layer | Responsibility |
|---|---|
| **AXIS OMNI** | Master orchestration, workflow state, approvals, routing, completion criteria |
| **AXIS** | Technical implementation, integrations, deployment, order routing |
| **VERITY** | Authorization, compliance, risk, claims, economics, verification |
| **DIRECTOR** | Positioning, listings, product pages, creative assets |
| **BEACON** | Demand analysis, measurement, profitability, next-best action |

The detailed 14-module architecture is preserved under [`prompts/modules`](prompts/modules), while the compressed five-role operating model is under [`prompts/roles`](prompts/roles).

## Repository map

```text
axis-omni-commerce/
├── prompts/
│   ├── AXIS_OMNI_MASTER_PROMPT.md
│   ├── roles/
│   └── modules/
├── schemas/
├── config/
├── docs/
├── examples/
├── assets/
├── src/
├── tests/
├── QUICKSTART.md
└── README.md
```

## Start here

1. Read [`QUICKSTART.md`](QUICKSTART.md).
2. Use [`prompts/AXIS_OMNI_MASTER_PROMPT.md`](prompts/AXIS_OMNI_MASTER_PROMPT.md) as the main system prompt.
3. Configure limits in [`config/policy.example.yaml`](config/policy.example.yaml).
4. Use the JSON schemas to force structured handoffs.
5. Run the first acceptance test in [`docs/ACCEPTANCE_CRITERIA.md`](docs/ACCEPTANCE_CRITERIA.md).

## Important boundary

This repository is an implementation framework, not proof of a profitable or fully autonomous business. Live deployment still requires authorized platform accounts, supplier agreements, secure credentials, compliant payment flows, and human approval for material legal or financial actions.

## Version

`1.0.0`

## License

No license has been selected. See [`LICENSE_NOT_SELECTED.md`](LICENSE_NOT_SELECTED.md).
