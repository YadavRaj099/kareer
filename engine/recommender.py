from engine.loader import load_json
from engine.scorer import score_career
from engine.similarity import find_similar_careers

CAREERS_FILE = "data/careers.json"
RULES_FILE = "data/scoring_rules.json"


# -----------------------------------
# CLASSIFY MATCH STRENGTH
# -----------------------------------

def classify(score, rules):

    thresholds = rules.get("classification", {})

    if score >= thresholds.get("perfect", 10):
        return "Perfect Match"

    elif score >= thresholds.get("strong", 8):
        return "Strong Match"

    elif score >= thresholds.get("alternative", 6):
        return "Alternative"

    elif score >= thresholds.get("weak", 3):
        return "Weak Match"

    return "Exploratory Match"


# -----------------------------------
# MAIN RECOMMENDATION ENGINE
# -----------------------------------

def recommend(user_answers, top_n=5):

    careers = load_json(CAREERS_FILE)
    rules = load_json(RULES_FILE)

    if not isinstance(careers, list):
        careers = []

    if not isinstance(user_answers, dict):
        user_answers = {}

    results = []

    # ----------------------------
    # SCORE ALL CAREERS
    # ----------------------------

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

    # ----------------------------
    # SORT CAREERS BY SCORE
    # ----------------------------

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    # ----------------------------
    # ENSURE RESULTS ALWAYS EXIST
    # ----------------------------

    if not ranked:
        return {
            "matches": [],
            "similar_careers": []
        }

    top_results = ranked[:top_n]

    # ----------------------------
    # FIND SIMILAR CAREERS
    # ----------------------------

    best_career = top_results[0].get("data", {})

    try:
        similar = find_similar_careers(best_career, careers)
    except Exception:
        similar = []

    # ----------------------------
    # SAFETY FALLBACK
    # ----------------------------

    if not top_results:
        top_results = ranked[:3]

    return {
        "matches": top_results,
        "similar_careers": similar
    }