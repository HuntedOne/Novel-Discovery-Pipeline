# Novel Psychedelic Discovery — Open-Source Computational Sandbox

A hands-on learning project for understanding the AI/computational pipeline behind
novel psychedelic (5-HT2A) compound discovery, built entirely on open-source tools.

> **What this is:** a guided, notebook-based sandbox to *learn what each tool does and
> how they hand off to each other.*
> **What this is not:** a production discovery engine, and it contains no synthesis
> chemistry. It supports research literacy only.

## Start here
1. Read `Psychedelic_Discovery_Pipeline_Reference.docx` — the conceptual map and the
   dated tool landscape this project is built from.
2. Skim `docs/background/00_README_reading_order.md` — the concept primers, in order.
3. Follow `docs/SETUP.md` to build the environment (Claude Code will generate this).
4. Run the notebooks in `notebooks/` in numerical order, starting with
   `00_environment_check.ipynb`.

## The pipeline at a glance
| Stage | Question | Notebook |
|------|----------|----------|
| 1 | What does the target look like? | `02_target_structure` |
| 2 | Does a molecule bind, how tightly? | `03_pockets`, `04_docking_classical`, `05_cofolding_affinity` |
| 3 | Agonist or antagonist? | (frontier — discussed in `06`) |
| 4 | Therapeutic vs. hallucinogenic signaling? | (frontier — discussed in `06`) |
| 5 | Selective and safe? | `07_admet_safety` |
| 6 | Drug-like / brain-penetrant? | `07_admet_safety` |
| 7 | What does it feel like? | **No tool. Human-clinical only.** |

Foundations live in `01_molecules_with_rdkit`; the capstone that chains stages is
`08_mini_pipeline`.

## Core principle
Prediction confidence is **high at the bottom of the causal chain (structure, binding)
and collapses as you climb toward function, signaling bias, and subjective experience.**
The notebooks make this gradient visible.

## Project layout
```
psychedelic-pipeline-project/
├── README.md                 ← you are here
├── CLAUDE.md                 ← instructions for Claude Code (the build spec)
├── Psychedelic_Discovery_Pipeline_Reference.docx
├── docs/
│   ├── SETUP.md              ← (generated) beginner install guide
│   └── background/           ← concept primers (read these first)
├── notebooks/                ← one per pipeline stage
├── src/                      ← shared helpers
└── data/                     ← precomputed fallbacks for heavy models
```

## A note on responsibility
Novelty is exactly what makes a compound's safety profile unknown. Moving from these
notebooks toward real compounds engages controlled-substance law and human-research
ethics — part of the pipeline, not an afterthought.
