import csv
from pathlib import Path
from .features import predict, risk_score

ROOT = Path(__file__).resolve().parents[1]

def load_rows():
    with (ROOT / "data/sample_urls.csv").open(newline="") as f:
        return [{**row, "label": int(row["label"])} for row in csv.DictReader(f)]

def metrics(rows, threshold=3):
    counts = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}
    for row in rows:
        actual, guess = row["label"], predict(row["url"], threshold)
        key = {(1, 1): "tp", (0, 0): "tn", (0, 1): "fp", (1, 0): "fn"}[(actual, guess)]
        counts[key] += 1
    precision = counts["tp"] / max(1, counts["tp"] + counts["fp"])
    recall = counts["tp"] / max(1, counts["tp"] + counts["fn"])
    accuracy = (counts["tp"] + counts["tn"]) / len(rows)
    return counts | {"accuracy": accuracy, "precision": precision, "recall": recall}

def main():
    rows = load_rows()
    result = metrics(rows)
    print("URL screening experiment")
    print("=" * 26)
    print("samples:", len(rows))
    print("accuracy: {accuracy:.1%}".format(**result))
    print("precision: {precision:.1%}".format(**result))
    print("recall: {recall:.1%}".format(**result))
    print("confusion:", {k: result[k] for k in ("tp", "tn", "fp", "fn")})
    print("\nExamples to inspect:")
    for row in rows:
        print(f"  {predict(row['url'])} score={risk_score(row['url'])}: {row['url']}")

if __name__ == "__main__":
    main()
