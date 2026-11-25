# Presentation Outline + 3-Minute Video Script
### Antibiotic Resistance Evolution Simulator · WUPENGHUI · INT6064 Individual Teaching Module

---

## PPT outline (≈12 slides, mirrors the rubric: objectives, sequence, assessment, materials, screenshots/code)

1. **Title** — "Antibiotic Resistance Evolution Simulator: a two-lesson module I built to teach computational thinking through biology." Name, ID, course.
2. **What this module is** — S4 (ages 15–16); a Python simulation of bacteria (S/R) evolving; two lessons; runs in Colab or offline.
3. **What I wanted them to learn** — Biology: natural selection → antibiotic resistance. CT: decompose the process, model it, test one variable, evaluate evidence.
4. **Why I built it this way** — invisible evolution made visible; a *simple, readable* model (students see the loop, not a black box); Python because the logic must be read and changed.
5. **How the two lessons run** — Lesson 1 build & predict; Lesson 2 experiment design & decision.
6. **Lesson 1 detail** — unplugged selection game → run default → predict vs observe → connect to natural selection (cost of resistance).
7. **Lesson 2 detail** — choose one variable → fair test → compare curves → CER → recommendation on antibiotic use.
8. **Where the computational thinking is** — decomposition / abstraction / algorithms / pattern recognition / evaluation / debugging (mapping table).
9. **How I check learning** — prediction sheet, one-variable table, graph description, CER paragraph, recommendation.
10. **Support, stretch, expected problems** — sentence starters (support); drift & mutation (stretch); misconceptions & responses.
11. **What's in the box / how to run** — `.ipynb` (Colab), `.py` (offline), teacher notes, prediction sheet, screenshots.
12. **Takeaway** — students do biology and computational thinking at the same time; the model is honest about its limits.

---

## 3-minute video script (target ≤ 3:00)

**[0:00–0:20] Problem + hook**
"Antibiotic resistance is evolution happening in hospital wards — and students can't see it.
In this lesson, my students run a tiny simulation and watch resistance evolve in seconds.
I'm [WUPENGHUI], and this is my individual teaching module."

**[0:20–0:55] Show the model (the algorithm)**
On screen: *[show the S/R bacteria and the three-step loop]*
"Each bacterium is either susceptible or resistant. Every generation has one loop:
selection, reproduction, record. Susceptible bacteria die when the drug is present;
resistant ones survive and pass on that trait. The loop runs — and the resistant
percentage climbs."

**[0:55–1:30] Live demo — full course**
Run the default (start 1% resistant):
"Watch: one percent at the start… and within a few generations it's nearly all resistant.
That's natural selection. This is the 'aha' moment my students predict first, then check."

**[1:30–2:05] Two more cases — cost & dose**
"Take the drug away and the resistant ones pay a cost, so resistance falls back — a fair
test of one variable. And a half dose still breeds resistance, just slower. So 'less
antibiotic' isn't automatically safer."

**[2:05–2:40] Student experiment**
"In lesson two, students change exactly one variable — population size here — predict,
run, and compare the curves. They write a claim, the evidence, and the reasoning.
Computational thinking is in every step: they decompose the process, read the algorithm,
spot the pattern, and evaluate."

**[2:40–3:00] So what**
"By the end, they can back up a real recommendation about antibiotic use with evidence
they produced themselves — biology and coding in one task. That's the module."

*(≈330 spoken words ≈ 2:45–3:00 at a measured pace.)*