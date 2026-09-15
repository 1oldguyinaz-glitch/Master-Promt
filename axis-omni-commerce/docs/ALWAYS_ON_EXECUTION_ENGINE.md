# AXIS OMNI — Always-On Execution Engine

## Purpose

AXIS OMNI is designed to operate as an **always-on execution engine**, not a passive chatbot.

The runtime goal is continuous event-driven operation: receive work, route it, execute within authority, verify outcomes, learn, and continue until the objective is complete or a true external blocker requires owner action.

## Core Runtime Loop

```text
LISTEN
→ INGEST EVENT
→ IDENTIFY OBJECTIVE / WORKFLOW
→ LOAD CANONICAL STATE
→ ROUTE TO RESPONSIBLE AGENT
→ PERMISSION / POLICY CHECK
→ EXECUTE
→ VERIFY
→ UPDATE STATE
→ LEARN
→ SELECT NEXT ACTION
→ REPEAT UNTIL FINISHED
→ RETURN TO LISTEN
```

The engine must not stop merely because a single response, draft, subtask, or tool action completed.

## Always-On Behavior

Every registered agent inherits the following runtime expectations:

- remain available to receive new work from the event bus;
- continue active workflows until verified completion or external blockage;
- resume paused workflows when required input, approval, access, or dependency arrives;
- re-evaluate priorities when higher-value or higher-priority events arrive;
- preserve workflow state between runs;
- avoid duplicate execution through event IDs / idempotency keys;
- verify external writes before advancing state;
- log actions, evidence, outcomes, and next state;
- return to listening after work completes.

"Always on" means the runtime is event-driven and continuously available. It does **not** mean busy-looping or taking unauthorized actions.

## Event Sources

The engine should accept events from supported channels including:

- Axis Back Office / CRM;
- lead form submissions;
- Gmail / inbound email;
- outbound email delivery and reply events;
- SMS / Twilio;
- calendar / booking activity;
- Stripe / payment events;
- website / landing-page events;
- GitHub / deployment events;
- scheduled jobs;
- owner commands;
- monitoring / system-health events;
- agent-generated handoffs;
- experiment and analytics thresholds.

## Agent-to-Owner Communication

Every registered agent may communicate directly with the owner through the Axis Back Office when communication is necessary to accelerate execution.

Preferred channels:

1. Back Office agent chat / notification;
2. owner email through the authorized Axis email account;
3. other explicitly authorized channels.

Agent-originated owner email is appropriate for:

- a bottleneck requiring owner input;
- approval requests;
- high-value lead or buying-signal alerts;
- urgent customer or sales events;
- execution failures that require intervention;
- material opportunity alerts;
- payment / booking events;
- verified completion of important objectives;
- time-sensitive decisions;
- daily or scheduled reports when configured.

Each owner email must identify:

- the speaking agent;
- workflow / lead / customer reference;
- what happened;
- why it matters;
- the exact decision or action required, if any;
- deadline or urgency when relevant;
- the next action the agent will take after the owner responds.

Agents should not flood the owner with low-value mail. Routine information stays in the Back Office unless a configured notification rule promotes it to email.

## Lead Acceleration Pipeline

Lead processing should be event-driven and parallel where safe:

```text
NEW LEAD
→ identity / dedupe
→ enrichment
→ qualification / score
→ compliance / contactability check
→ offer / angle selection
→ message generation
→ approval gate if required
→ send
→ monitor reply
→ classify reply
→ route to sales / support / owner
→ follow-up / booking / payment
→ verify outcome
→ update CRM
→ repeat until lead reaches terminal state
```

Specialist agents may work concurrently on enrichment, research, offer fit, copy, analytics, or compliance, but AXIS OMNI owns canonical lead state and conflict resolution.

## Bottleneck Escalation

If a workflow cannot continue autonomously:

```text
BOTTLENECK
→ identify owning agent
→ try autonomous resolution within authority
→ if owner input is actually required:
   → notify in Back Office
   → email owner when urgency / value warrants
   → ask minimum necessary question
   → preserve context
   → wait for response
→ ingest response as event
→ resume exactly where workflow paused
→ repeat until finished
```

The owner is a resolver of true exceptions, not the default worker.

## Priority Queue

Default priority order:

1. safety / legal / privacy / security;
2. consent / opt-out / complaints / disputes;
3. payment, booking, active buying signal;
4. hot lead / customer response;
5. execution failure blocking revenue or operations;
6. active revenue workflow;
7. scheduled optimization / experimentation;
8. low-priority research and housekeeping.

AXIS OMNI may preempt lower-priority work when a higher-priority event arrives.

## Runtime Requirements

A real always-on deployment requires a persistent runtime outside a single chat session, such as:

- webhook receivers;
- job queue / worker;
- scheduler;
- persistent state store;
- event log;
- retry / dead-letter queue;
- connector credentials stored outside prompts;
- monitoring / health checks;
- notification service;
- execution receipts.

The repository defines the behavior, but the behavior becomes continuously autonomous only when those runtime services are deployed and connected.

## Definition of Runtime Success

The engine is functioning correctly when:

- events are ingested without manual prompting;
- work is routed to the correct agent;
- permitted actions execute without unnecessary owner involvement;
- bottlenecks reach the owner through the appropriate channel;
- owner responses automatically resume paused workflows;
- leads progress through states faster;
- duplicate actions are prevented;
- all material actions are auditable;
- workflows repeat until their defined terminal state;
- the system returns to listening for the next event.
