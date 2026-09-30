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
## Project reflection

- **What I personally implemented:** I wrote the lexical feature extractor, the weighted risk-scoring algorithm, the prediction threshold, the benchmark metrics, the synthetic labeled dataset, and the unit tests.
- **One actual result:** On the 14-example dataset, the detector reached **85.7% accuracy, 100.0% precision, and 71.4% recall**; all **3 tests passed**.
- **One unexpected result:** The detector missed suspicious-looking examples with many path segments or a shortened-looking path, showing that an intuitive signal is not automatically a useful signal in a small rule system.
- **One limitation:** This result cannot establish real-world phishing-detection performance because the dataset is small, synthetic, and not evaluated on live or time-separated URLs.
- **Next iteration:** I intend to evaluate a larger licensed dataset with a time-based split and compare the rules against logistic regression while keeping an error-analysis table.
