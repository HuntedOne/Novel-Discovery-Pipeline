# Primer 8 — A DevOps primer for the tooling beginner

**Used by:** whenever an install or environment thing confuses you.

You know Python. This primer covers the *tooling around* Python that ML tools assume you
know — the part that breaks installs and wastes afternoons.

## Virtual environments — why your installs fight each other
Different tools need different, sometimes conflicting, versions of the same library. A
**virtual environment** is an isolated box of packages for one project, so Project A's
needs don't break Project B's. Always work inside one. Two common managers:
- **conda** (used by `environment.yml`): handles non-Python dependencies too (compilers,
  CUDA libraries). Best for the heavy scientific tools here.
- **pip + venv** (used by `requirements-light.txt`): Python-only; lighter. Fine for the
  CPU/light path.

This project gives you both: a conda `environment.yml` for the full path and a
`requirements-light.txt` for the everywhere-runs path.

## conda vs pip — the short version
Use **conda** to create the environment and install the tricky binary stuff (RDKit, CUDA
toolkit). Use **pip** inside it for pure-Python packages not on conda. Mixing them
carelessly is the #1 cause of broken environments — install conda things first, pip
things after, and don't switch back and forth.

## GPUs and CUDA — why some notebooks need a special machine
The deep models (Boltz-2, OpenFold-3, DiffDock) run realistically only on a **GPU** — a
graphics processor that does the massively parallel math these models need. **CUDA** is
NVIDIA's software layer that lets Python talk to the GPU. If versions of CUDA, the GPU
driver, and PyTorch don't match, the tool silently falls back to CPU (very slow) or
errors. This is normal and frustrating; the SETUP guide pins compatible versions.

**The light path in this project deliberately needs no GPU.** Heavy notebooks ship
precomputed results in `data/` so you can learn the concepts on any laptop, then run the
real model later if you get GPU access (a cloud instance, a lab machine, Colab).

## What a Jupyter notebook/kernel actually is
A **notebook** (`.ipynb`) interleaves runnable code cells with text. A **kernel** is the
Python process behind it — it must be the one *inside your project's environment*, or
your installed packages won't be found. If imports fail despite installing, you're almost
certainly on the wrong kernel. (Notebook 00 checks exactly this.)

## When an install breaks — a calm checklist
1. Are you in the right environment? (`conda activate <env>` / venv activated.)
2. Is the notebook using that environment's kernel?
3. Did you install conda things before pip things?
4. For GPU tools: do `nvidia-smi`, your CUDA, and your PyTorch build agree?
5. Still stuck? Use the light path + precomputed data and move on — don't let setup
   block the learning.
