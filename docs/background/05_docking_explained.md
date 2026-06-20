# Primer 5 — Docking explained

**Used by:** notebooks 03, 04, 05.

## What docking does
Docking predicts **how** and **how well** a small molecule (ligand) fits into a protein
pocket. Two outputs:
- a **pose** (the 3D arrangement of the ligand in the pocket), and
- a **score** (a rough estimate of binding favorability).

## You usually need the pocket first
Blind docking aside, most workflows first locate the binding site. **P2Rank** (ML-based)
and **fpocket** (geometry-based) predict pockets from structure. Notebook 03 covers this.
*Cryptic pockets* — sites that only appear when the protein moves — are a frontier and
the reason ensemble/cofolding methods are interesting.

## Two families of docking tools
1. **Classical (physics/empirical):** **AutoDock Vina** (Apache-2.0) is the open
   workhorse — fast, well-understood, great for learning and for large virtual screens.
   **Gnina** adds a CNN rescorer on the Vina/Smina lineage.
2. **Machine-learning / diffusion:** **DiffDock-L** (MIT) predicts poses via a diffusion
   model and can dock "blind" (no pre-specified pocket). Powerful, but **watch
   generalization** to novel scaffolds, and **validate poses** — ML methods sometimes
   produce physically invalid geometries. The **PoseBusters** benchmark exists precisely
   to catch this.

## The caveat that must be loud
**A docking score is not a binding affinity, and neither is an effect.** Scores are
noisy and best used to *rank and triage*, not to declare a binder. And nothing in
docking tells you agonist vs. antagonist (Primer 2). Notebook 04 demonstrates this by
docking known ligands and showing how scores rank them only roughly.

## How it hands off
Pocket (03) → dock known/generated ligands (04) → for the deep version, cofold +
affinity with Boltz-2 (05) → push survivors to ADMET/safety (07).
