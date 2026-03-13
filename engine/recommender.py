from engine.loader import load_json
from engine.scorer import score_career

CAREERS_FILE = "data/careers.json"
RULES_FILE = "data/scoring_rules.json"


def classify(score, rules):

    thresholds = rules["classification"]

    if score >= thresholds["perfect"]:
        return "Perfect Match"

    elif score >= thresholds["strong"]:
        return "Strong Match"

    elif score >= thresholds["alternative"]:
        return "Alternative"

    elif score >= thresholds["weak"]:
        return "Weak Match"

    return "Not Recommended"


def recommend(user_answers, top_n=5):

    careers = load_json(CAREERS_FILE)
    rules = load_json(RULES_FILE)

    results = []

    for career in careers:

        score = score_career(career, user_answers, rules)

        classification = classify(score, rules)

        results.append({
            "career": career.get("name"),
            "score": score,
            "classification": classification,
            "data": career
        })

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    return ranked[:top_n]