import re, json
from collections import Counter

def tokenize(t: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9\+#\.]+", (t or "").lower())

def score(resume_text: str, jd_text: str) -> dict:
    rtok = Counter(tokenize(resume_text))
    jtok = Counter(tokenize(jd_text))
    required = {w for w,c in jtok.items() if c>=2}  # crude keyword importance
    present = {w for w in required if w in rtok}
    missing = sorted(required - present)
    coverage = 0 if not required else round(100 * len(present)/len(required))
    length_ok = 450 <= len(resume_text) <= 5000
    sections_ok = all(s in resume_text.lower() for s in ["experience","education","skills"])
    score = min(100, max(0, coverage + (10 if length_ok else 0) + (10 if sections_ok else 0)))
    return {"score": score, "coverage": coverage, "missing_keywords": missing,
            "checks": {"length_ok": length_ok, "sections_ok": sections_ok}}
