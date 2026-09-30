# Can Simple Rules Detect Suspicious URLs?

A small, reproducible experiment comparing transparent URL heuristics with a weighted lexical risk score. The goal is not to claim that one toy detector can protect the internet; it is to investigate which URL signals are useful, where they fail, and how false positives appear.

## Research question

> Do simple, explainable URL features separate obviously benign and suspicious examples well enough to be useful as a first screening layer?

## Curiosity prompts

- Do long URLs really look more suspicious in this dataset?
- Which signal creates the most false positives?
- Does combining several weak signals outperform one strong rule?
- Which examples does the detector get wrong, and why?

## Run it

```bash
python3 -m src.benchmark
python3 -m unittest discover -s tests -v
```

The benchmark uses a small synthetic dataset in `data/sample_urls.csv`. No live URLs are requested or visited. This is an educational classifier, not a browser security product.

## Project structure

- `src/features.py` — deterministic lexical feature extraction
- `src/benchmark.py` — baseline rules, weighted score, and metrics
- `data/sample_urls.csv` — synthetic labeled examples
- `tests/` — unit tests for feature extraction and scoring

## What I learned / next steps

This experiment is intentionally modest. A useful next step would be to evaluate a larger, licensed dataset and compare these rules with logistic regression using a time-based split so that domains from the future do not leak into training.

## Safety

The examples are synthetic. Do not test URLs against systems you do not own or have permission to assess.
