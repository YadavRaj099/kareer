from engine.loader import load_json
from engine.scorer import score_career
from engine.similarity import find_similar_careers

CAREERS_FILE = "data/careers.json"
RULES_FILE = "data/scoring_rules.json"


def classify(score, rules):

    thresholds = rules.get("classification", {})

    if score >= thresholds.get("perfect", 10):
        return "Perfect Match"

    elif score >= thresholds.get("strong", 8):
        return "Strong Match"

    elif score >= thresholds.get("alternative", 6):
        return "Alternative"

    elif score >= thresholds.get("weak", 4):
        return "Weak Match"

    return "Not Recommended"


def recommend(user_answers, top_n=5):

    careers = load_json(CAREERS_FILE)
    rules = load_json(RULES_FILE)

    if not isinstance(careers, list):
        careers = []

    results = []

    for career in careers:

        if not isinstance(career, dict):
            continue

        score = score_career(career, user_answers, rules)

        classification = classify(score, rules)

        results.append({
            "career": career.get("name", "Unknown Career"),
            "score": score,
            "classification": classification,
            "data": career
        })

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    top_results = ranked[:top_n]

    if top_results:
        best_career = top_results[0]["data"]
        similar = find_similar_careers(best_career, careers)
    else:
        similar = []

    return {
        "matches": top_results,
        "similar_careers": similar
    }