# Primer 2 — Binding vs. efficacy vs. signaling bias

**Used by:** every notebook. This is the conceptual spine of the project.

If you take one idea from this project, take this one:

> **Binding is not activation. Activation is not direction. None of them is experience.**

## Three separate questions
1. **Binding (occupancy):** does the molecule sit in the pocket, and how tightly?
   Measured as affinity (Ki, Kd, IC50 → often expressed as pKi/pIC50). *This is what
   docking and cofolding tools predict best.*
2. **Efficacy (function):** once bound, does it *activate* the receptor (agonist),
   *block* it (antagonist), or *partially* activate it (partial agonist)? Two molecules
   can dock almost identically and do opposite things. **Frontier — poorly predicted
   from structure alone.**
3. **Signaling bias (functional selectivity):** the receptor couples to more than one
   downstream pathway — notably **Gq protein** vs. **β-arrestin**. A "biased" agonist
   pushes one pathway over the other. **The leading hypothesis for separating a
   compound's therapeutic effects from its hallucinogenic ones is that you can bias the
   signaling.** This is the field's central open question and its hardest prediction
   problem.

## Why this matters for *your* goal
The thing you'd most like to predict — "is this a safer, more therapeutic variant?" —
lives at the **bias** level (question 3), which is exactly where computational
prediction is weakest. Meanwhile docking scores (question 1) are seductively easy to
generate and *look* like answers. A notebook that ranks molecules by docking score is
ranking them by question 1 while implying question 3. Don't fall for it; the notebooks
flag this everywhere.

## Polypharmacology — the "character" layer
Even among 5-HT2A agonists, the *character* of the experience (not whether it's
psychoactive, but what it's like) is shaped by the **full off-target fingerprint** —
5-HT1A, 5-HT2C, dopamine D2, and others — plus binding *kinetics* (LSD sits in the
pocket for hours). To infer character you'd need accurate affinity predictions across
*dozens* of targets at once, and errors compound across that panel.

## The confidence gradient (memorize this shape)
```
structure ▰▰▰▰▰  high confidence
binding   ▰▰▰▰   
affinity  ▰▰▰    
efficacy  ▰▰     frontier
bias      ▰      frontier
character ▱      very low
experience ✗     no computational proxy at all
```
