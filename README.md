# Antibiotic Resistance Evolution Simulator

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/felixxxxx11/antibiotic-resistance-sim/blob/main/Antibiotic_Resistance_Sim.ipynb)

A small, runnable model of how **antibiotic resistance evolves by natural selection** in a
population of bacteria — built as an **INT6064 Individual Teaching Module** (two-lesson
secondary STEM module: Biology + Mathematics + Computational Thinking).

Students run the model, change **one variable at a time**, and use the resulting
frequency-vs-generation graphs as **evidence** to make a real recommendation about
antibiotic use.

## ▶ Live demo — no login, no install

Open **https://felixxxxx11.github.io/antibiotic-resistance-sim/simulator.html** and click **Run simulation**.

To run offline, just **double-click `simulator.html`** — it works in any browser, no Python or account needed.

---

## What the model does

A population of `N` bacteria carries one of two genotypes:

- `S` = susceptible to the antibiotic
- `R` = resistant

Each generation repeats one loop:

1. **Selection** — bacteria reproduce in proportion to their *fitness* in the current
   environment (antibiotic on / off).
2. **Reproduction** — `N` parents are sampled (weighted by fitness); each child inherits
   the parent genotype (with an optional mutation rate).
3. **Record** — the percentage of resistant bacteria is logged for that generation.

That loop is the algorithm; students read it, rather than trusting a black box.

## Quick start

**Online (no install):** click the "Open in Colab" badge above, then run the cells top to bottom.

**Offline:**

```bash
pip install -r requirements.txt   # optional – only needed for the plot
python3 antibiotic_resistance_sim.py --plot
```

The model itself uses only the Python standard library; `matplotlib` is optional (only for plots).

## Example scenarios (built into the script)

| Scenario | What students see |
|---|---|
| Full antibiotic course | Resistance rises to ~100% within a few generations |
| No antibiotic (start high) | Resistance *falls* — the cost of resistance |
| Sub-lethal / half dose | Resistance still rises, just more slowly |
| Small population | Genetic drift — the trait can be lost by chance |

## Repository layout

```
Antibiotic_Resistance_Sim.ipynb   # main artifact (open in Colab)
antibiotic_resistance_sim.py      # same model as an offline script
teacher_materials/                # lesson plan, CT map, assessment, misconceptions, limitations
figures/                          # example output plots
docs/                             # slide outline + 3-minute video script
```

## The two-lesson module

- **Lesson 1 — Build & predict:** an unplugged selection game → run the default model →
  predict before observing → connect to natural selection (and the cost of resistance).
- **Lesson 2 — Experiment & decide:** change one variable (starting %, dose, population
  size, generations) → fair test → compare curves → CER explanation → evidence-based
  advice on antibiotic use.

## Computational thinking

Decomposition · Abstraction · Algorithm design · Pattern recognition · Evaluation · Debugging —
all embedded in the activity and mapped in `teacher_materials/Teacher_Notes.md`.

## Limitations (model honesty)

The model tracks **frequencies**, not absolute population size, so it shows *why* resistance
evolves but not the full within-body infection dynamics. Fitness values are teaching values,
not clinical data. These limits are discussed with students.

---

*Author: WUPENGHUI (11729730) — INT6064 Coding and Computational Thinking, Individual Teaching Module.*