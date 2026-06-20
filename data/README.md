# data/ — precomputed fallbacks

Heavy notebooks (esp. 05 Boltz-2, and any GPU step) must run on a laptop *conceptually*
even when the real model can't. Claude Code should populate this folder with small
precomputed outputs and document each file here:

- `boltz2_precomputed.csv` — affinity estimates for the known ligands (notebook 05 fallback)
- `pocket_residues.json` — predicted 5-HT2A pocket residues (notebook 03 fallback)
- `vina_scores.csv` — docking scores for known ligands (notebook 04 fallback)
- `reinvent_runlog.csv` — a tiny generation run log (notebook 06 fallback)

Keep these small and clearly labeled as illustrative.
