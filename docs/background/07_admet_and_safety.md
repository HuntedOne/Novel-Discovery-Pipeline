# Primer 7 — ADMET and safety filtering

**Used by:** notebook 07 (and as a scoring component in 06).

## What ADMET means
**A**bsorption, **D**istribution, **M**etabolism, **E**xcretion, **T**oxicity — the
properties that decide whether a molecule could ever be a usable drug, separate from
whether it hits the target. This stage is comparatively **mature** and well-tooled.

## The safety liabilities that matter most here
For any serotonergic agonist program, screen early for:
- **5-HT2B agonism →** associated with **cardiac valvulopathy** (heart valve damage).
  A classic reason to demand *selectivity* against 5-HT2B.
- **hERG channel block →** cardiac arrhythmia risk. A near-universal early tox filter.
- **Blood-brain-barrier (BBB) penetrance →** a CNS compound that can't cross the BBB is
  inert for these purposes; you need predicted penetrance.

## Open tools
- **ADMET-AI (MIT):** fast graph-neural-network predictions across many ADMET endpoints,
  including hERG and BBB. Pairs naturally as a REINVENT scoring component.
- **RDKit (BSD):** computes the descriptor-based rules of thumb (Lipinski, TPSA, logP)
  that give a first-pass drug-likeness read.
- **DeepChem (MIT):** broader ML-for-chemistry toolkit if you want to build custom models.

## How notebook 07 uses these
It takes known ligands (and any molecules from notebook 06) and builds a **candidate
scorecard**: affinity signal + selectivity flags (5-HT2B/hERG) + BBB + drug-likeness.
This scorecard is the closest the sandbox comes to "is this worth a closer look" — and
the notebook is explicit that it stops well short of "is this safe" or "what does it do."

## The honest ceiling
ADMET models predict *liabilities and properties*, not the **subjective or therapeutic
effect** (Stage 7 — the wall). A clean ADMET profile means "developable," not "good."
