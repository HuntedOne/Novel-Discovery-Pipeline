# Background reading — suggested order

These primers give you the concepts needed to use the tools effectively. Read them
roughly in this order. Each is short and points to where it's used in the notebooks.

1. **`01_gpcr_and_5ht2a.md`** — How the target receptor works. (Foundational.)
2. **`02_binding_vs_efficacy_vs_bias.md`** — The single most important distinction in
   this whole project. Why a docking score is not an effect.
3. **`03_cheminformatics_basics.md`** — SMILES, fingerprints, similarity. What RDKit
   gives you. Needed for notebook 01.
4. **`04_structure_prediction_and_cofolding.md`** — AlphaFold lineage, OpenFold-3,
   Boltz-2, Chai-1. What "cofolding" means.
5. **`05_docking_explained.md`** — Classical (Vina) vs ML (DiffDock) docking; poses,
   scoring, pockets. Needed for notebooks 03–05.
6. **`06_generative_design.md`** — How REINVENT and pocket-based generators work; the
   generate→score→optimize loop. Needed for notebook 06.
7. **`07_admet_and_safety.md`** — ADMET, hERG, 5-HT2B, BBB. The safety filters. Needed
   for notebook 07.
8. **`08_devops_primer.md`** — For the tooling beginner: environments, conda vs pip,
   GPUs/CUDA, what a Jupyter kernel is, why installs break. Read whenever an install
   confuses you.
9. **`09_reading_new_developments.md`** — The meta-skill: how to evaluate a new model or
   paper and place it on the pipeline. Your durable takeaway.

> All scientific claims here are introductory and meant to orient you toward primary
> sources (lab papers, tool docs), not replace them.
