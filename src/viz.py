"""
Shared helpers for the psychedelic-pipeline notebooks.

Kept deliberately small and well-commented. Claude Code should expand this as the
notebooks grow (e.g. add docking-box helpers, scorecard builders). The point of having
this file is so notebooks stay readable and the user sees reusable patterns.
"""
from __future__ import annotations


def show_structure(pdb_path: str, width: int = 700, height: int = 450,
                   highlight_resids: list[int] | None = None):
    """Render a PDB structure with py3Dmol; optionally highlight pocket residues.

    Parameters
    ----------
    pdb_path : path to a .pdb file (e.g. the 5-HT2A structure from notebook 02)
    highlight_resids : residue numbers to draw as sticks (e.g. predicted pocket)
    """
    import py3Dmol
    with open(pdb_path) as fh:
        pdb = fh.read()
    view = py3Dmol.view(width=width, height=height)
    view.addModel(pdb, "pdb")
    view.setStyle({"cartoon": {"color": "spectrum"}})
    if highlight_resids:
        view.addStyle({"resi": [str(r) for r in highlight_resids]},
                      {"stick": {"colorscheme": "orangeCarbon"}})
    view.zoomTo()
    return view


def mol_from_smiles(smiles: str):
    """Parse SMILES to an RDKit mol with a clear error if it fails (SMILES is fragile)."""
    from rdkit import Chem
    m = Chem.MolFromSmiles(smiles)
    if m is None:
        raise ValueError(f"RDKit could not parse SMILES: {smiles!r}")
    return m


def confidence_banner(stage: str, level: str, why: str) -> str:
    """Return a printable banner used in the capstone to make the confidence gradient visible.

    level: 'HIGH' | 'MEDIUM' | 'LOW' | 'NONE'
    """
    mark = {"HIGH": "█████", "MEDIUM": "███··", "LOW": "█····", "NONE": "·····"}.get(level.upper(), "?????")
    return f"[{mark}] {stage}: CONFIDENCE {level.upper()} — {why}"
