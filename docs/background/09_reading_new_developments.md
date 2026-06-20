# Primer 9 — How to read new developments (the durable skill)

**Used by:** your brain, every time you see a new model or paper.

The tools will change. This skill won't. When you encounter a new model, paper, or
product announcement, run it through this filter.

## Step 1 — Place it on the pipeline
Which of the seven stages does it touch?
1. Structure · 2. Binding · 3. Efficacy · 4. Signaling bias · 5. Selectivity · 6. ADMET
· 7. Subjective experience.

Stages 1, 2, 6 are mature → improvements are **incremental**.
Stages 3, 4, 5 are frontier → credible improvements are **valuable**.
Stage 7 → **be skeptical of any claim**; there is no computational proxy.

## Step 2 — Ask the four diagnostic questions
1. **Which stage?** (above)
2. **Out-of-distribution performance?** Does it report results on compounds/targets
   *dissimilar* to training data? That's the only number that matters for novel
   discovery. If they only show easy in-distribution cases, discount the hype.
3. **Function/bias, or just structure/affinity?** Predicting *that it binds* is far
   easier than *what it does*. A tool claiming reliable **efficacy or signaling-bias**
   prediction from structure is the kind of thing that would actually move the field —
   look hard at the evidence.
4. **Independent, held-out benchmark?** Prefer community benchmarks (PoseBusters, Runs N'
   Poses, DockGen) over self-reported metrics. Who built the test set, and could the
   model have seen it?

## Step 3 — Check the access reality
Open weights + code (like Boltz-2, OpenFold-3, REINVENT) you can actually use. The best
engines are often proprietary (e.g. IsoDDE) — impressive, but not a tool *you* can run.
For a small team, the open/smaller-model track is where your leverage is.

## Step 4 — Find the caveat the press release buried
Every real tool has one: false-positive rates, narrow training distribution, validity
failures, "predicts affinity not efficacy." If a write-up has no caveats, that's itself a
red flag.

## The one-sentence test
> *"Does this credibly improve an out-of-distribution prediction at Stage 3, 4, or 5,
> on an independent benchmark, with usable access?"*

If yes — pay close attention. If no — it's probably incremental or hype.
