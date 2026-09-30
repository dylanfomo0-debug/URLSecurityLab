from __future__ import annotations
from urllib.parse import urlparse
import ipaddress

SUSPICIOUS_WORDS = {"login", "verify", "account", "password", "secure", "urgent", "update", "bank"}

def extract(url: str) -> dict[str, float]:
    parsed = urlparse(url)
    host = parsed.hostname or ""
    try:
        ipaddress.ip_address(host)
        has_ip = 1.0
    except ValueError:
        has_ip = 0.0
    lowered = url.lower()
    return {
        "length": float(len(url)),
        "dots": float(url.count(".")),
        "hyphens": float(url.count("-")),
        "at_symbol": float("@" in url),
        "query_marks": float(url.count("?")),
        "path_depth": float(len([p for p in parsed.path.split("/") if p])),
        "has_ip": has_ip,
        "not_https": float(parsed.scheme != "https"),
        "suspicious_words": float(sum(word in lowered for word in SUSPICIOUS_WORDS)),
    }

def risk_score(url: str) -> int:
    f = extract(url)
    score = 0
    score += int(f["has_ip"] * 3)
    score += int(f["at_symbol"] * 3)
    score += int(f["not_https"] * 1)
    score += int(f["suspicious_words"] >= 2) * 2
    score += int(f["length"] >= 70)
    score += int(f["path_depth"] >= 5)
    return score

def predict(url: str, threshold: int = 3) -> int:
    return int(risk_score(url) >= threshold)
