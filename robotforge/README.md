# RobotForge — Child Geofence Wearable (prototype)

This is the first vertical proof-of-concept for **RobotForge**, an MCP/ChatGPT plugin that designs a buildable device, exposes a verified bill of materials, and tests system behavior. This project does **not** track a child or send live alerts yet.

## User story

A guardian selects a distance from a **fixed saved location**, such as home or school. An LTE-M + GNSS wearable periodically reports authenticated location updates to a **private guardian service**. Two consecutive trustworthy fixes entirely beyond the radius (including the GNSS uncertainty band) cause the guardian app to send an urgent notification. An independent connection-loss alarm fires when reports are stale. A parent-phone-moving-radius mode is future work because it requires reliable phone background location and separate synchronization.

## Reference hardware for bench prototype (not child-ready)

- Circuit Dojo **nRF9151 Feather**, manufacturer list price $69 USD as checked Oct 2026: https://www.circuitdojo.com/products/nrf9151-feather
- Manufacturer-listed compatible **LTE + GPS combo antenna**, $8 as checked: same source
- Manufacturer-listed Hologram IoT SIM, $3 for the SIM card itself; **data plan and carrier coverage not included**: same source
- Manufacturer-approved protected rechargeable battery, charging hardware, strain relief and properly tested enclosure: **prices and compatibility not yet verified**
- App/backend: secure authenticated account, private location store, push notifications, no public live map.

**Do not place an exposed development board, antenna cable, or bare lithium battery on a child's body.** First test on a desk with simulated movement and in an adult-carried, professionally enclosed prototype. Use appropriate breakaway/clip design; avoid necklaces or unsafe constrictive straps. Waterproofing, charging safety, heating, mechanical retention and regulatory obligations need verification before daily wear.

### Key engineering constraints

- Outdoor GPS accuracy varies; walls and roofs can block satellite positioning. A 50-ft geofence is configurable but cannot be advertised as precise or instantaneous.
- Position reports require working cellular service; LTE-M plans and carrier certification must be verified for the chosen modem and location.
- Send locations to the guardian's **authenticated private backend**, **not** into the ChatGPT plugin. This plugin accepts only **synthetic distances and accuracy values** to test the geofence logic.
- App alerts have inevitable network, GNSS acquisition, and push-delivery latency. Display the timestamp/accuracy of the last fix and independently alarm on missing data.
- Allow verified guardians to set zones, revoke access, and delete location history; encrypt in transit and at rest. Track the minimum data needed.
- This is a supplemental safety tool, not a fail-safe personal safety system.

## Plugin tools

- \`design_wearable\`: returns a reference engineering specification and explicit missing validation steps.
- \`simulate_geofence\`: processes *synthetic* relative distance/accuracy updates with a conservative uncertainty band, rejecting stale fixes.
- \`compare_quotes\`: optimizes quoted part subtotal + combined supplier shipping, once per supplier, and refuses unpriced freight. All quotes must come from external verified supplier data; **no integrated live catalog yet**.

## Quickstart

Python 3.10+ required.

\`\`\`bash
python -m pip install -r robotforge/requirements.txt
python robotforge/server.py
\`\`\`

Then connect the MCP endpoint at \`http://localhost:8000/mcp\` from a supported MCP client (expose over HTTPS, add authentication, and disable public location processing before deployment). For offline logic checks:

\`\`\`bash
python -m unittest discover -s robotforge -p 'test_*.py' -v
\`\`\`

ChatGPT custom plugins use MCP: https://developers.openai.com/plugins/build/mcp-server

## Production backlog

1. Confirm LTE-M/GNSS and power with a certified SIM in the target coverage area.
2. Replace bench components with a lightweight custom PCB and tested, sealed enclosure; account for skin contact, battery safety, mechanical hazards.
3. Implement end-to-end device authentication, nonce/replay protection, secure OTA firmware updates, and TLS.
4. Implement an independent backend service that detects boundaries and sends APNs/FCM pushes plus optional SMS fallback; check OS delivery restrictions.
5. Add indoor fallback methods (Wi-Fi or BLE presence) and "last known fix" uncertainty labels.
6. Verify GNSS error distribution, battery life, end-to-end alert latency, false positives and missed exits in field trials.
7. Wire up permitted supplier catalogs and compute **landed cost** (part cost, taxes, shipping, quantities, service fees).
8. Run security, child safety and privacy reviews before any real-world use.

## Acceptance criteria for a field-ready iteration

- Geofence settings retained per authorized caregiver; no location leaks to ChatGPT or public URLs.
- Two consecutive high-quality fixes confirm exits; isolated drift does not trigger an exit alarm.
- Disconnect/low-battery alarms independent of the exit detector.
- Real-world test establishes p50/p95 alert latency and exit detection sensitivity before release.
- User sees stale/uncertain location status instead of invented live precision.
