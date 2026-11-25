"""
Antibiotic Resistance Evolution Simulator
=========================================
A small, runnable model for a two-lesson secondary biology / mathematics / CT module.

Idea
----
A population of bacteria carries one of two genotypes:
    'S' = susceptible to an antibiotic
    'R' = resistant to the antibiotic

Each generation:
    1. SELECTION  - bacteria reproduce in proportion to their fitness in the current
                    environment (antibiotic ON or OFF).
    2. REPRODUCTION - N parents are sampled (weighted by fitness); each child inherits
                    the parent genotype (optionally with a small mutation rate).
    3. RECORD    - the frequency of resistant bacteria is logged for that generation.

This is a compact "Wright-Fisher" style model. It is deliberately simple so that
secondary students can see the mechanism of natural selection and antibiotic
resistance without molecular detail.

Assumptions (discuss these with students):
    * fixed population size (N stays constant each generation),
    * only two genotypes ('S' / 'R'), selected on by relative fitness,
    * fitness values are ILLUSTRATIVE TEACHING VALUES, not clinical data,
    * no immune system, no spatial structure, no horizontal gene transfer.
    The model explains *why* resistance evolves by selection; it is not medical advice.

No third-party libraries are required to run the model itself. If matplotlib is
available, a plot is also saved for the classroom.

Usage
-----
    python3 antibiotic_resistance_sim.py                 # run the built-in scenarios
    python3 antibiotic_resistance_sim.py --scenario C     # run one scenario
    python3 antibiotic_resistance_sim.py --n 2000 --gens 80 --seed 7

Author: (student) - INT6064 Individual Teaching Module
"""

from __future__ import annotations
import random
import argparse
from dataclasses import dataclass
from typing import Callable, List


# ----------------------------------------------------------------------------
# Fitness settings (relative reproductive success)
# ----------------------------------------------------------------------------
# When there is NO antibiotic, resistant bacteria pay a small "cost" -> 0.95.
# When the antibiotic is ON, susceptible bacteria are strongly suppressed -> 0.15,
# while resistant bacteria keep almost full fitness -> 0.95.
# These numbers are teaching values, not clinical constants.
@dataclass
class Fitness:
    s_no_abx: float = 1.00   # susceptible, no antibiotic
    r_no_abx: float = 0.95   # resistant, no antibiotic  (cost of resistance)
    s_on_abx: float = 0.15   # susceptible, antibiotic ON (they die)
    r_on_abx: float = 0.95   # resistant, antibiotic ON

    def weights(self, antibiotic_on: bool):
        if antibiotic_on:
            return self.s_on_abx, self.r_on_abx
        return self.s_no_abx, self.r_no_abx


# ----------------------------------------------------------------------------
# Core simulation
# ----------------------------------------------------------------------------
def run_simulation(
    n: int = 1000,
    generations: int = 40,
    f0_resistant: float = 0.01,
    antibiotic_schedule: Callable[[int], bool] = lambda g: True,
    mutation_rate: float = 0.0,
    fitness: Fitness | None = None,
    seed: int | None = 1,
) -> List[float]:
    """Run the model and return the resistant frequency at each generation."""
    if fitness is None:
        fitness = Fitness()
    rng = random.Random(seed)

    # initial population
    n_res = round(n * f0_resistant)
    population: List[str] = ["R"] * n_res + ["S"] * (n - n_res)

    history: List[float] = []

    for gen in range(generations):
        abx = antibiotic_schedule(gen)
        wS, wR = fitness.weights(abx)
        weights = [wR if gt == "R" else wS for gt in population]

        # record frequency at the start of each generation
        history.append(population.count("R") / len(population))

        # reproduction: sample N parents weighted by fitness, inherit genotype
        new_pop = rng.choices(population, weights=weights, k=len(population))

        # optional mutation (flip genotype with small probability)
        if mutation_rate > 0:
            for i, gt in enumerate(new_pop):
                if rng.random() < mutation_rate:
                    new_pop[i] = "S" if gt == "R" else "R"

        population = new_pop

    history.append(population.count("R") / len(population))
    return history


def average_runs(runs: int = 5, **kwargs) -> List[float]:
    """Run the model `runs` times (different seeds) and return the average frequency curve."""
    import random as _random
    total = None
    for i in range(runs):
        h = run_simulation(seed=_random.randint(0, 1 << 30), **kwargs)
        total = h if total is None else [x + y for x, y in zip(total, h)]
    return [x / runs for x in total]


# ----------------------------------------------------------------------------
# Scenarios used in the lesson
# ----------------------------------------------------------------------------
def scenarios():
    """Return a dict of named scenarios: (history, description)."""
    # A. Full, continuous antibiotic course -> resistance rises to fixation
    a = run_simulation(n=1000, generations=40, f0_resistant=0.01,
                       antibiotic_schedule=lambda g: True, seed=1)
    # B. No antibiotic at all -> resistance slowly declines (cost of resistance)
    b = run_simulation(n=1000, generations=40, f0_resistant=0.50,
                       antibiotic_schedule=lambda g: False, seed=1)
    # C. Weak selection throughout -> resistance still rises, just more slowly
    #    than strong selection. Communicate as "weak selection scenario",
    #    not as a medical dose recommendation.
    c = run_simulation(n=1000, generations=40, f0_resistant=0.01,
                       antibiotic_schedule=lambda g: True,
                       fitness=Fitness(s_on_abx=0.60, r_on_abx=0.95), seed=1)
    # D. Small population -> drift / stochastic loss is visible
    d = run_simulation(n=50, generations=40, f0_resistant=0.30,
                       antibiotic_schedule=lambda g: False, seed=3)
    return {
        "A": (a, "Full continuous antibiotic course (N=1000, start R=1%)"),
        "B": (b, "No antibiotic (N=1000, start R=50%) -> cost of resistance"),
        "C": (c, "Weak selection scenario (N=1000, start R=1%) -> resistance still rises, more slowly"),
        "D": (d, "Small population, no antibiotic (N=50, start R=30%) -> genetic drift"),
    }


# ----------------------------------------------------------------------------
# Text output helpers (no dependencies)
# ----------------------------------------------------------------------------
def ascii_trend(history: List[float], width: int = 40) -> str:
    """A tiny ASCII bar chart of resistant frequency over generations."""
    lines = []
    for gen, f in enumerate(history):
        if gen % 2 != 0:   # print every other generation to keep it compact
            continue
        bar = "#" * int(round(f * width))
        lines.append(f"  gen {gen:>2} | {bar:<{width}} {f*100:5.1f}%")
    return "\n".join(lines)


def print_scenario(key, history, desc):
    final = history[-1]
    print(f"\n[{key}] {desc}")
    print(f"    final resistant frequency: {final*100:.1f}%")
    print(ascii_trend(history))


def try_plot(all_results):
    """Save a line plot if matplotlib is available; otherwise skip."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        print("\n(matplotlib not available - skipping plot; text output above is enough.)")
        return
    plt.figure(figsize=(7, 4))
    for key, (hist, desc) in all_results.items():
        plt.plot(range(len(hist)), [100 * x for x in hist], label=f"Scenario {key}")
    plt.xlabel("Generation")
    plt.ylabel("Resistant bacteria (%)")
    plt.title("Evolution of antibiotic resistance (teaching model)")
    plt.legend()
    plt.tight_layout()
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "resistance_scenarios.png")
    plt.savefig(out, dpi=130)
    print(f"\nSaved plot -> {out}")


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Antibiotic resistance evolution simulator")
    ap.add_argument("--scenario", choices=["A", "B", "C", "D"], help="run one scenario")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--gens", type=int, default=40)
    ap.add_argument("--f0", type=float, default=0.01, help="initial resistant frequency 0-1")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--plot", action="store_true", help="save a matplotlib plot")
    args = ap.parse_args()

    if args.scenario is None and args.n == 1000 and args.gens == 40 \
       and args.f0 == 0.01 and args.seed == 1:
        # default: run all four built-in scenarios
        results = scenarios()
        print("=" * 70)
        print("ANTIBIOTIC RESISTANCE EVOLUTION SIMULATOR - built-in scenarios")
        print("=" * 70)
        for key, (hist, desc) in results.items():
            print_scenario(key, hist, desc)
        if args.plot:
            try_plot(results)
        return

    # custom run
    hist = run_simulation(n=args.n, generations=args.gens, f0_resistant=args.f0,
                          antibiotic_schedule=lambda g: True, seed=args.seed)
    print(f"Custom run: N={args.n}, gens={args.gens}, startR={args.f0*100:.1f}%")
    print_scenario("custom", hist, "continuous antibiotic, custom parameters")


if __name__ == "__main__":
    main()