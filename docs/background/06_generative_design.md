# Primer 6 — Generative molecular design

**Used by:** notebook 06.

## The idea
Instead of screening an existing library, **generative models invent new candidate
structures** aimed at a goal. Two broad styles:
- **String/graph generators** that emit SMILES (e.g. **REINVENT 4**).
- **3D, pocket-conditioned generators** (diffusion models like SGEDiff, TopMT-GAN) that
  shape molecules to a specific binding site. Newer, less battle-tested.

## REINVENT 4 — the mature open option
**REINVENT 4 (Apache-2.0, maintained by AstraZeneca's Molecular AI)** is the practical
entry point. It supports de novo generation, scaffold decoration, linker design, R-group
replacement, and molecule optimization, using **reinforcement and curriculum learning**.

### The generate → score → optimize loop (the key concept)
1. The model **generates** a batch of molecules.
2. A **scoring function** rates each one — this is *your* design objective. It can combine
   docking scores, a Boltz-2 affinity estimate, ADMET predictions, similarity to a known
   scaffold, drug-likeness, etc. REINVENT's scoring is pluggable.
3. The scores are used as a **reward** to nudge the model toward higher-scoring regions.
4. Repeat. Over many epochs, generated molecules drift toward your objective.

Notebook 06 runs a *tiny* version of this loop with a simple scoring function so you can
*watch* molecules evolve — the point is to understand the mechanism, not to discover.

## The caveats that must be loud
- **It generates structures, not experiences.** A molecule that scores well on your
  reward is a *hypothesis*, nothing more.
- **Reward hacking is real:** generators exploit weaknesses in the scoring function,
  producing molecules that game the metric without being good candidates. Inspect output.
- **Training-data bias** constrains what it can explore — yet exploring *outside* known
  chemistry is exactly where novel-psychedelic value (and prediction unreliability) lies.
- **SMILES fragility** (Primer 3) applies.

## The ADMETrix pattern
A documented approach couples REINVENT (generation) with **ADMET-AI** (property/tox
scoring) so molecules are optimized for safety/drug-likeness from the start. Notebook 06
points toward this; notebook 07 builds the ADMET piece.
