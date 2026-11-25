# Short Descriptive Paragraph (Artifact) — 150–300 words

**Antibiotic Resistance Evolution Simulator** is a small Python program I wrote for a
two-lesson Secondary 4 biology module (ages 15–16). Students run a population of
bacteria in which each individual is either *susceptible* or *resistant* to an antibiotic.
Each generation, bacteria reproduce in proportion to their fitness in the current
environment: when the antibiotic is present, susceptible bacteria are largely removed
while resistant ones survive; when it is absent, resistant bacteria pay a small survival
cost. The program records the percentage of resistant bacteria over time, so students
see natural selection produce antibiotic resistance in front of them.

The artifact addresses a real STEM problem — how antibiotic misuse drives resistance —
and links Biology (inheritance and natural selection) with Mathematics (probability,
sampling, frequency and rates) and Computing. The pedagogical intention is for students
to *read the model*, not just run it: they decompose the process into selection,
reproduction and recording; they change **one variable at a time** (starting frequency, selection strength, population size); and they use the resulting graph as evidence to justify a
recommendation about antibiotic use. Computational thinking is therefore embedded in the
activity rather than added on top: abstraction (a bacterium reduced to a genotype),
algorithmic thinking (the generation loop), pattern recognition (rising/falling curves,
fixation) and evaluation (comparing scenarios).

Known limitations are discussed openly with students: the model tracks frequencies, not
total population size, and its fitness values are illustrative rather than clinical, so it
shows *why* resistance evolves but not the full within-body infection dynamics.

*Word count: ~235*
