WATCHLIST IMPORT FOLDER

Purpose:
Standalone import package for cryptocurrency watchlist data.
This does NOT modify TPI calculations, watchlist logic, or project architecture.

Current populated file:
- coinbase_watchlist_import.csv
- 209 assets from Coinbase's official US (incl. NY) Trading Assets disclosure
- Snapshot updated September 10, 2026

Secondary file:
- coinbase_watchlist_import.json (template; CSV is the ready import file)

CSV columns:
- name
- symbol
- coinbase_tradable
- network
- asset_type
- centralization_class

Important:
Coinbase's public Explore page currently shows a broader 409-410 'Tradeable' asset universe. That broader Explore universe is not identical to Coinbase's official US trading disclosure. The CSV intentionally uses the official US trading set rather than mixing in custody-only or region-dependent assets.

Design rule:
This folder is data-only. No TPI engine code belongs here.
