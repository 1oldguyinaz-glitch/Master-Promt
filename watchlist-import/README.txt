WATCHLIST IMPORT FOLDER

Purpose:
Standalone import package for cryptocurrency watchlist data.
This does NOT modify TPI calculations, watchlist logic, or project architecture.

Files expected in this folder:
- coinbase_watchlist_import.csv
- coinbase_watchlist_import.json

CSV columns:
- name
- symbol
- coinbase_tradable
- network
- asset_type
- centralization_class

Design rule:
This folder is data-only. No TPI engine code belongs here.
