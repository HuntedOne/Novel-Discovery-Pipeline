# Primer 1 — GPCRs and the 5-HT2A receptor

**Used by:** notebooks 02, 03, 04, 05.

## The big picture
Classic serotonergic psychedelics — LSD, mescaline, psilocin (the active form of
psilocybin), DMT — produce their characteristic effects mainly by activating the
**serotonin 5-HT2A receptor**. Block that receptor with a selective antagonist
(ketanserin) and the psychedelic experience largely disappears in humans. So 5-HT2A
agonism is *necessary* for the classic effect — though, as Primer 2 explains, far from
*sufficient* to explain it.

## What a GPCR is
5-HT2A is a **G-protein-coupled receptor (GPCR)** — a protein that threads through the
cell membrane seven times (hence "7-transmembrane"). A molecule (the *ligand*) binds in
a pocket on the outside-facing part; this nudges the receptor into a new shape; that
shape change is relayed to the inside of the cell, triggering downstream signaling.

Key idea: **a GPCR is not a light switch but a shape-shifter.** It flexes between
*active* and *inactive* conformations (and several in between). Which shape a ligand
stabilizes determines what signal gets sent. This is why "what does the receptor look
like" (Stage 1) and "in which state" matters so much.

## Why 5-HT2A is a good running example
- It is heavily studied, with public experimental structures (search the PDB).
- Its pharmacology is comparatively well-mapped (the Roth lab's PDSP database has
  binding data for many ligands across many receptors).
- Its agonists span chemotypes — phenethylamines (mescaline), tryptamines (psilocin),
  ergolines (LSD) — giving you natural worked examples.

## A distinction to hold onto
**MDMA is mechanistically different.** It is primarily a *monoamine releaser* acting at
transporters (the serotonin transporter, SERT), not chiefly a direct 5-HT2A agonist.
Lumping it with LSD and mescaline will mislead any modeling. Model it separately.

## Where this shows up in the tools
- Stage 1 tools (OpenFold-3, Boltz-2) predict the 5-HT2A *structure*.
- Stage 2 tools dock ligands into its *pocket*.
- The hardest questions (Primer 2) are about which *conformation/signal* results.
