# BEACON Historical Signal Patch

Apply this patch to BEACON on every product-ranking and next-product cycle.

1. Load `prompts/subsystems/BEACON_HISTORICAL_SIGNAL_STORE.md`.
2. Load current signal data from `data/historical_signals/`.
3. Treat historical evidence as a prior, never as proof of current demand.
4. Compare historical signals against current supplier, market, platform, and economics evidence.
5. For every ranked candidate return:
   - historical_signal_match (0-100)
   - historical_signal_reasons
   - fresh_evidence_strength (0-100)
   - historical_fresh_conflict (true/false)
   - exploit_or_explore (EXPLOIT|EXPLORE)
   - updated_confidence
   - next_learning_value
6. VERITY authorization, compliance, fulfillment, and economics gates always override historical signal strength.
7. After every real experiment, write the observed result back into the historical signal store so future rankings compound evidence instead of restarting research.
