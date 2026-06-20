# CLAUDE.md — Project instructions for Claude Code

> This file tells Claude Code what to build and how. It is written to be handed
> directly to `claude` in this directory. Read it fully before acting.

## Who this is for
The owner is a **non-physician psychedelic researcher** with:
- **Intermediate Python** (comfortable with functions, classes, pandas, plotting).
- **Beginner DevOps/tooling** (new to environments, CUDA, package conflicts, CLI ML tools).

So: prefer **clear, heavily-commented, runnable code** over clever code. Explain every
new tool the first time it appears. Assume the user learns by running cells and reading
output, not by reading source.

## The goal of this project
Build a **hands-on learning sandbox** that walks through the computational pipeline for
novel psychedelic discovery, one stage at a time, using **open-source tools only**.
The deliverable is a set of **Jupyter notebooks** (one per pipeline stage) plus the
supporting environment, that let the user *see what each tool does and how the tools hand
off to each other*. This is a **learning instrument, not a production discovery engine.**

The scientific framing, stage maturity, and tool choices are specified in
`Psychedelic_Discovery_Pipeline_Reference.docx` (in this directory) and summarized in
`docs/background/`. **Read the background docs before writing notebooks.**

## Hard constraints (do not violate)
1. **No synthesis chemistry.** Nothing about how to physically make any compound.
2. **Use the 5-HT2A receptor as the running example target.** It is well-studied and
   public (e.g. PDB structures exist). Use known public ligands (LSD, mescaline,
   psilocin, serotonin) as worked examples — these are reference data, not products.
3. **Every notebook must teach, not just run.** Each begins with a markdown cell stating:
   which pipeline stage, what question it answers, the tool's maturity rating, and the
   key caveat. Each ends with a "What you should now understand" recap and a
   "Where this hands off to next" pointer.
4. **Label confidence honestly.** Where a tool's output is unreliable (efficacy, bias,
   subjective effects), say so in the notebook, prominently. Do not let the sandbox imply
   that a docking score predicts an experience.
5. **Graceful degradation.** Heavy models (Boltz-2, OpenFold-3, DiffDock) may not fit the
   user's hardware. Every notebook that uses a heavy model must (a) detect GPU/CPU, and
   (b) provide a small precomputed-results fallback in `data/` so the *concepts* are
   learnable even without the model running. Building these fallbacks is part of the task.

## Build order (do these in sequence)
1. **Environment first.** Create `environment.yml` (conda) AND a `requirements-light.txt`
   for the no-GPU subset (RDKit, AutoDock Vina, P2Rank, ADMET-AI, pandas, py3Dmol).
   Document the install in `docs/SETUP.md` with the "light path" (CPU, runs anywhere)
   vs "full path" (GPU, runs the deep models) clearly separated. Explain conda vs pip,
   what a virtual environment is, and what CUDA is — the user is a DevOps beginner.
2. **Smoke-test notebook** `notebooks/00_environment_check.ipynb` — verifies imports,
   prints versions, detects GPU, downloads one small example structure. If this passes,
   the user knows their setup works before tackling the science.
3. **One notebook per stage** (see "Notebook plan" below). Build them in pipeline order.
   Each must run end-to-end on the light path OR fall back to precomputed data.
4. **A capstone notebook** `notebooks/08_mini_pipeline.ipynb` that chains 2–3 stages on a
   single example so the user sees the handoffs as one flow.
5. **Update `docs/background/` as you go** if you introduce a concept not yet covered.

## Notebook plan (titles, stage, primary tool, learning aim)
Create these in `notebooks/`. Numbers set run order.

- `00_environment_check.ipynb` — Setup smoke test. RDKit + py3Dmol. Aim: confirm install, learn what a notebook + kernel is.
- `01_molecules_with_rdkit.ipynb` — *Foundations.* RDKit. Aim: SMILES, drawing, descriptors, similarity. Compare LSD vs mescaline vs psilocin vs serotonin fingerprints. **Build this first and thoroughly — everything downstream needs it.**
- `02_target_structure.ipynb` — *Stage 1.* Fetch a public 5-HT2A structure; visualize with py3Dmol; discuss active vs inactive states. Light path uses a downloaded PDB; show where OpenFold-3/Boltz would predict it.
- `03_pockets.ipynb` — *Stage 2/5.* P2Rank + fpocket. Aim: find and visualize the binding pocket; concept of cryptic/allosteric sites.
- `04_docking_classical.ipynb` — *Stage 2.* AutoDock Vina (+ Gnina if available). Dock the known ligands into the pocket; read poses and scores; **caveat: pose ≠ affinity ≠ efficacy.**
- `05_cofolding_affinity.ipynb` — *Stage 2 (deep).* Boltz-2. Aim: joint structure + affinity from sequence+SMILES. **Full path only; ships precomputed outputs as fallback.** Contrast with classical docking from notebook 04.
- `06_generative_design.ipynb` — *Stage 3/4.* REINVENT 4. Aim: run a tiny generation loop with a simple scoring function; watch molecules evolve toward a property. **Caveat: generates structures, not experiences.**
- `07_admet_safety.ipynb` — *Stage 5/6.* ADMET-AI + RDKit filters. Aim: screen generated/known molecules for hERG, BBB, 5-HT2B-type liabilities; build a candidate scorecard.
- `08_mini_pipeline.ipynb` — *Capstone.* Chain: known ligand → pocket → dock → ADMET scorecard. Show the handoffs and where confidence drops.

## Style requirements for notebooks
- First cell: markdown header with Stage / Question / Maturity / Caveat box.
- Liberal markdown between code cells explaining *why*, not just *what*.
- Print shapes/types/heads so the user sees the data.
- Every plot/3D view labeled.
- No silent failures: wrap heavy model calls in try/except that fall back to `data/` and
  print a clear message about why.
- End cell: "What you should now understand" + "Hands off to: <next notebook>".

## Deliverables checklist
- [ ] `environment.yml`, `requirements-light.txt`
- [ ] `docs/SETUP.md` (beginner-grade, light vs full path)
- [ ] All 9 notebooks above, runnable on light path or with fallback data
- [ ] `data/` precomputed fallbacks for heavy stages (05, and any GPU step)
- [ ] `src/` for any shared helper functions (e.g. a `viz.py` for py3Dmol wrappers)
- [ ] `docs/background/` kept in sync with concepts introduced
- [ ] A top-level `README.md` orienting a newcomer (you may expand the existing one)

## When unsure
Ask the user, or default to the **simpler, more explained, lighter-weight** option.
This project's success metric is *the user understands what each tool does and how they
interact* — not benchmark performance.
