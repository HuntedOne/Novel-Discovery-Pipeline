# SETUP — installation guide

> Beginner-grade on purpose. If a step confuses you, read
> `docs/background/08_devops_primer.md` first — it explains what a virtual
> environment, a kernel, conda vs pip, and CUDA actually are.

This project has **three install paths**. Almost everything you need to learn is
on the **light path** — start there.

| Path | Runs on | Covers | When to use |
|------|---------|--------|-------------|
| **Light** | Any laptop, no GPU (incl. Apple Silicon Mac) | 00, 01, 02, 03, 04, 07, 08 — and 05/06 from precomputed `data/` | **Start here.** Everything except *running* the heavy deep models. |
| **Colab** | Google Colab (free/cheap cloud GPU) | Actually *running* 05 (Boltz-2) and 06 (REINVENT 4) | When you want to see the GPU-only models execute, but don't own a GPU. |
| **Full** | Linux + NVIDIA GPU + CUDA | Everything, locally | Only if you have an NVIDIA GPU box. |

---

## Light path (recommended start — verified on macOS Apple Silicon)

This is the path this project was built and tested on: **Python 3.11**, a virtual
environment, and pip.

### 1. Get Python 3.11
Your Mac's built-in `python3` is older (3.9) and not ideal. Install 3.11 with
[Homebrew](https://brew.sh):

```bash
brew install python@3.11
```

(Linux: `sudo apt install python3.11 python3.11-venv`. Windows: install Python
3.11 from python.org and use `py -3.11` below.)

### 2. Create and activate a virtual environment
A *virtual environment* (`.venv`) is a private, project-local copy of Python so
this project's packages never collide with anything else on your machine.

```bash
cd "path/to/psychedelic-pipeline-project"
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
```

Your shell prompt should now show `(.venv)`. Everything below runs *inside* it.
Re-run the `source ...` line in every new terminal.

### 3. Install the light-path packages
```bash
pip install --upgrade pip
pip install -r requirements-light.txt
```

### 4. Register the Jupyter kernel
A *kernel* is the Python process Jupyter runs your cells in. This line makes your
`.venv` selectable inside the notebooks:

```bash
python -m ipykernel install --user --name psychedelic-pipeline \
  --display-name "Python (psychedelic-pipeline)"
```

### 5. Launch and verify
```bash
jupyter lab
```
Open `notebooks/00_environment_check.ipynb`, and in the top-right **select the
"Python (psychedelic-pipeline)" kernel**. Run every cell. If they all pass, your
setup is good — go to notebook 01.

> **If imports fail despite installing:** you are almost certainly on the wrong
> kernel (the default one, not `psychedelic-pipeline`). Switch it via
> *Kernel → Change Kernel*. See `docs/background/08_devops_primer.md`.

---

## Standalone (non-pip) tools — needed from notebook 03 onward

Some tools are **not** Python packages, so `pip` can't install them. Install
these when you reach the notebook that needs them; each notebook also falls back
to precomputed `data/` so you're never blocked.

| Tool | Needed by | macOS (Homebrew) | What it is |
|------|-----------|------------------|------------|
| **fpocket** | nb 03 | `brew install fpocket` | Compiled C; geometric pocket finder. |
| **P2Rank** | nb 03 | `brew install openjdk` then download P2Rank from its [releases](https://github.com/rdk/p2rank/releases) | A Java app — needs a JRE (that's what `openjdk` provides). |
| **AutoDock Vina** | nb 04 | `brew install autodock-vina` | The classical docking binary; Python calls it via a wrapper. |
| **meeko** (pip) | nb 04 | `pip install meeko` | Prepares ligands (PDBQT) for Vina. |
| **ADMET-AI** (pip) | nb 07 | `pip install admet-ai` | Safety/ADMET model. Pulls CPU **torch + chemprop** — a large (~1–2 GB) download; expect a few minutes. |

(Linux: `apt install fpocket autodock-vina default-jre`. Windows: use the Colab
path or WSL2 for these — native Windows installs are fiddly.)

---

## Colab path (run the GPU-only models without owning a GPU)

Notebooks **05 (Boltz-2)** and **06 (REINVENT 4)** need an NVIDIA GPU, which a Mac
doesn't have. To run them for real:

1. Go to [colab.research.google.com](https://colab.research.google.com) and open
   the notebook (upload it, or open from a GitHub/Drive copy).
2. **Runtime → Change runtime type → GPU** (a free T4 is enough for the small
   demos here).
3. At the top of the notebook, install the heavy deps in the Colab session:
   ```python
   !pip install -q rdkit boltz            # notebook 05
   # notebook 06: follow the REINVENT 4 install in docs/background/06_generative_design.md
   ```
4. Upload the small input files the notebook needs (the notebook says which), or
   mount your Drive.

> On the light path you don't need any of this — notebooks 05 and 06 detect the
> absence of a GPU and load the precomputed results from `data/` so you still see
> and understand the outputs.

---

## Full path (Linux + NVIDIA GPU only)

If you have an NVIDIA GPU box, one conda environment does everything:

```bash
conda env create -f environment.yml      # see the CUDA note inside the file
conda activate psychedelic-pipeline
python -m ipykernel install --user --name psychedelic-pipeline
jupyter lab
```

`environment.yml` pins CUDA 12.1; edit `pytorch-cuda` to match your driver if
conda can't resolve it, or follow the current command at https://pytorch.org/.

---

## Verifying your install
Open and run `notebooks/00_environment_check.ipynb`. If every cell passes, you're
set. The notebook prints your Python version, which packages are present, and
whether a GPU was detected — so it doubles as a quick diagnostic if a later
notebook misbehaves.
