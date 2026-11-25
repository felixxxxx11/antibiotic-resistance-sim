# Teacher Notes — Antibiotic Resistance Evolution Simulator

**INT6064 Individual Teaching Module** · two-lesson secondary STEM module
**Subject focus:** Biology (inheritance & evolution / antibiotic resistance) + Mathematics (probability, data) + Computing (CT)
**Target learners:** Secondary 4, ages 15–16 (adaptable to S3–S5)
**Duration:** 2 × 45-minute lessons
**Platform:** Python (Google Colab / Jupyter; also runs offline with plain Python 3)

---

## 1. What the module is

Students use a small, runnable simulation of a bacterial population to see **evolution by natural selection** happen in real time. Each bacterium is *susceptible* (`S`) or *resistant* (`R`) to an antibiotic. Each generation the program:
1. lets bacteria reproduce in proportion to their **fitness** in the current environment (antibiotic on/off),
2. produces the next generation by weighted random sampling,
3. records the **percentage of resistant bacteria**.

Students predict, run, change **one variable**, and compare the resulting frequency-vs-generation curves. The endpoint is an evidence-based recommendation about **how antibiotics should be used** — connecting a coding model to a real public-health issue.

The model is deliberately *simple* so that the **mechanism is visible** and the **code is readable**. Students are not asked to trust a black box; they read the loop.

---

## 2. Learning objectives

By the end of the module students can:
1. **Explain** how selection changes the frequency of a trait in a population (natural selection → antibiotic resistance).
2. **Read and describe** a frequency-vs-generation graph, including *when* and *how fast* resistance rises.
3. **Design a fair test** by changing one variable (starting frequency, selection strength, population size, number of generations) and predicting the outcome first.
4. **Interpret data** to justify a recommendation about antibiotic use (transfer beyond the simulation).

---

## 3. Computational thinking map

| CT concept | Where it appears in the module |
|---|---|
| **Decomposition** | Breaking the process into: selection → reproduction → recording. |
| **Abstraction** | A bacterium is modelled only by its genotype (`S`/`R`); molecular detail is ignored. |
| **Pattern recognition** | Rising/falling curves; *fixation* (100%); *loss* of a trait; effect of selection strength. |
| **Algorithm design** | The per-generation loop; the fair-test procedure; the plotting routine. |
| **Evaluation** | Comparing scenarios; judging which treatment strategy keeps resistance lowest. |
| **Debugging** | When a result looks wrong (e.g., % > 100 or a flat line), students trace the logic. |
| **Data practices** | Recording parameters and outputs in a table (one-variable table). |

---

## 4. Lesson 1 — Build & understand the model (45 min)

| Time | Activity |
|---|---|
| 0–10 | **Hook / unplugged selection game.** Each student holds a card `S` or `R`. The teacher is the "antibiotic": roll a die — `S` bacteria die on most rolls, `R` survive. Which genotype is left? Introduce the question. |
| 10–20 | **Model the process together.** On the board, write the loop: *selection → reproduction → record*. This is decomposition + algorithm in plain English. |
| 20–35 | **Run the default simulation** (notebook §2). Students first **write a prediction** (e.g., "1% resistant will…"), then run and compare with the grey/actual curve. Discuss: *why does it rise so fast?* |
| 35–45 | **Connect to natural selection.** Record findings on the prediction sheet. Introduce the "cost of resistance" idea (notebook §3, no-antibiotic curve falls). |

**Product of Lesson 1:** completed prediction sheet + annotated first graph.

---

## 5. Lesson 2 — Experiment design & decision (45 min)

| Time | Activity |
|---|---|
| 0–5 | Recall the Lesson-1 finding. Pose the driving question: *what does this imply for how we should use antibiotics?* |
| 5–15 | **Choose ONE variable** (starting %, selection strength, population size, generations). Students fill in a one-variable table (what I change / what I keep the same / my prediction). |
| 15–30 | **Run and compare** (notebook §4–§5, or multiple scenarios). Students capture the curve and note the final resistant %. |
| 30–40 | **CER explanation:** Claim – Evidence – Reasoning. Then a short evidence-based **recommendation** ("take the full prescribed course", "don't use leftover antibiotics", etc.). |
| 40–45 | Share-out: groups compare which variable had the biggest effect on resistance. |

**Product of Lesson 2:** one-variable table + comparison graph + CER paragraph + recommendation.

---

## 6. Scaffolding & differentiation

- **Support:** start with the default run only; prompt cards with sentence starters ("When the antibiotic was on, the resistant % ____ because ____"); pre-filled parameter cell.
- **Core:** full one-variable experiment + CER paragraph.
- **Stretch:** combine two runs to compare selection strengths (a *strategy* discussion, not a dosing recommendation); explore the **small-population (drift)** case and explain why chance matters; repeat a run several times and average it to reduce randomness; in the **Python script** (not the browser UI) you can set `mutation_rate > 0` to discuss how resistance can appear from nothing.

---

## 7. Assessment (formative)

- Prediction sheet (committed *before* each run — discourages pure trial-and-error).
- One-variable table (control of variables).
- Frequency-vs-generation graph with a written description.
- CER paragraph linking claim, evidence and reasoning.
- Final recommendation to a real audience (e.g., a poster for the school).

---

## 8. Common misconceptions & responses

| Misconception | Response / evidence |
|---|---|
| "The antibiotic *creates* resistant bacteria." | Resistance already exists at a low frequency; the drug **selects** for it. Show the starting 1% and the curve rising. |
| "Bacteria 'decide' to become resistant." | There is no decision — it is differential survival/reproduction (run the unplugged game). |
| "Resistance always rises." | Start high, no antibiotic → the **cost** makes resistance *fall* (notebook §3). |
| "Small and large populations behave the same." | Run `n = 50` vs `n = 1000` → drift in small populations. |
| "A lower dose is always better." | The weak-selection curve still rises — *slower*, but still toward resistance. This model does **not** give dosing advice. |

---

## 9. Technical deployment

- **Online:** open `Antibiotic_Resistance_Sim.ipynb` in Google Colab and run cells top to bottom (no installation).
- **Offline:** run `antibiotic_resistance_sim.py` with Python 3 (`python3 antibiotic_resistance_sim.py --plot`). Only the optional plot needs `matplotlib`; the model itself uses only the standard library.
- One device per pair is enough; students can alternate between running and recording.

---

## 10. Known limitations (model honesty)

- It models **frequencies**, not absolute population size, so it does **not** show the infection "clearing" or "coming back".
- Fitness values are **teaching values**, not clinical data.
- Space, host immune response and gene transfer are not modelled.
- These limits are **discussed with students** — a model is a deliberate simplification, and its assumptions matter.
- Because reproduction uses weighted random sampling, the same parameters can give slightly different curves across runs. Have students **repeat runs** and average them (or use the HTML simulator's "Run several times" control) before drawing conclusions.
