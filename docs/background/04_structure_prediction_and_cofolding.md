# Primer 4 — Structure prediction and cofolding

**Used by:** notebooks 02, 05.

## The lineage
- **AlphaFold 2 (2021):** predicted protein structure from sequence — a landmark.
- **AlphaFold 3 (2024):** extended to *complexes* — proteins with ligands, DNA, RNA.
  Won the 2024 Nobel Prize in Chemistry lineage. Caveat: accuracy drops on inputs
  *unlike* its training data (the out-of-distribution problem — the recurring theme).
- **Open reproductions (2025–26):** **OpenFold-3** (Apache-2.0, aims for AF3 parity),
  **Chai-1**, **Protenix** — open alternatives so you don't need proprietary access.

## What "cofolding" means
Older tools predicted the protein alone, then you docked a ligand into it separately.
**Cofolding** predicts the protein *and* ligand *together* — the pocket can flex to
accommodate the ligand (induced fit), which is more realistic than docking into a rigid
receptor.

## Boltz-2 — the standout for this project
**Boltz-2 (MIT license, open: weights + inference + training code)** is the first open
cofolding model to *jointly* predict complex structure **and small-molecule binding
affinity** from sequence + SMILES. Reported to approach the accuracy of physics-based
free-energy-perturbation (FEP) calculations at ~1000× the speed. It outputs two affinity
signals: a binder-vs-decoy classifier (good for triage) and a quantitative affinity
estimate (pIC50, for ranking).

**Important caveats (state them in the notebook):**
- Roughly 40% of its predicted "hits" can be false positives — it triages, doesn't
  confirm.
- It predicts *affinity*, **not efficacy or signaling bias** (Primer 2). A high Boltz-2
  affinity does not tell you agonist vs. antagonist, let alone therapeutic vs.
  hallucinogenic.
- The newer hosted "Boltz 2.1" is closed-source; the open package remains fully usable.

## Conformational states
For a GPCR like 5-HT2A, *which* state you model (active vs. inactive) shapes everything
downstream. Watch for tools that predict *ensembles* of states, not a single snapshot —
that capability is what the bias question (Primer 2) eventually needs.
