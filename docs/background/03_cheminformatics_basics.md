# Primer 3 — Cheminformatics basics (RDKit)

**Used by:** notebook 01 (and everywhere a molecule appears).

## SMILES — text that encodes a molecule
A **SMILES** string is a compact text representation of a molecular structure, e.g.
serotonin is `NCCc1c[nH]c2ccc(O)cc12`. You'll paste SMILES into nearly every tool.
RDKit turns a SMILES string into a molecule object you can analyze and draw.

Caveat worth knowing early: SMILES is fragile — a string can be valid text but invalid
chemistry, and the same molecule has many valid SMILES (canonicalization fixes this).
Generative tools that emit SMILES (REINVENT) inherit this fragility.

## Descriptors — numbers that summarize a molecule
RDKit computes **descriptors**: molecular weight, logP (lipophilicity), number of
hydrogen-bond donors/acceptors, topological polar surface area (TPSA), rotatable bonds.
These feed the classic "drug-likeness" rules of thumb (e.g. Lipinski) and matter for
brain penetrance (Primer 7).

## Fingerprints & similarity — how "alike" two molecules are
A **fingerprint** encodes a molecule as a bit-vector of substructures. Comparing two
fingerprints (Tanimoto similarity, 0–1) tells you how structurally similar molecules
are. This is how you'll see that LSD, mescaline, and psilocin occupy different regions of
chemical space despite sharing a receptor — and it's the backbone of "scaffold" thinking
(phenethylamines vs. tryptamines vs. ergolines).

## Why this is the foundation
Every downstream tool consumes molecules: docking needs a 3D ligand, generative models
emit SMILES, ADMET models featurize structures. Notebook 01 builds this fluency first on
purpose. **RDKit (BSD-licensed, open) is the library; you'll use it constantly.**
