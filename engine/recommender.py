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

    if score >= thresholds.get("perfect", 12):
        return "Perfect Match"

    elif score >= thresholds.get("strong", 9):
        return "Strong Match"

    elif score >= thresholds.get("alternative", 6):
        return "Alternative"

    elif score >= thresholds.get("weak", 3):
        return "Weak Match"

    return "Exploratory Match"


# -----------------------------------
# CONFIDENCE SCORE
# -----------------------------------

def confidence(score):

    # Convert score into percentage confidence
    base = min(95, 50 + score * 5)

    return round(base)


# -----------------------------------
# GENERATE EXPLANATION
# -----------------------------------

def explain_match(career, user_answers):

    explanation = []

    tags = career.get("tags", [])
    tags = [str(t).lower() for t in tags]

    stream = user_answers.get("stream")
    if stream and stream in tags:
        explanation.append("Your academic stream aligns with this career.")

    skills = user_answers.get("skills", [])
    for skill in skills:
        if skill in tags:
            explanation.append(f"Your interest in {skill} supports this career.")
            break

    interests = user_answers.get("interests", [])
    for interest in interests:
        if interest in tags:
            explanation.append(f"You selected {interest} as an interest area.")
            break

    work_style = user_answers.get("work_style")
    if work_style and work_style in tags:
        explanation.append("Your preferred work style matches this career.")

    if not explanation:
        explanation.append("Your responses show alignment with this field.")

    return explanation


# -----------------------------------
# LOAD CAREERS SAFELY
# -----------------------------------

def load_careers():

    data = load_json(CAREERS_FILE)

    if isinstance(data, dict):
        return data.get("careers", [])

    if isinstance(data, list):
        return data

    return []


# -----------------------------------
# MAIN RECOMMENDATION ENGINE
# -----------------------------------

def recommend(user_answers, top_n=5):

    careers = load_careers()
    rules = load_json(RULES_FILE)

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

        explanation = explain_match(career, user_answers)

        results.append({
            "career": career.get("name", "Unknown Career"),
            "score": score,
            "confidence": confidence(score),
            "classification": classification,
            "explanation": explanation,
            "data": career
        })

    # ----------------------------
    # SORT CAREERS BY SCORE
    # ----------------------------

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    # ----------------------------
    # GUARANTEE RESULTS
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
    # FALLBACK SIMILAR CAREERS
    # ----------------------------

    if not similar and len(ranked) > 3:
        similar = [r["data"] for r in ranked[3:6]]

    return {
        "matches": top_results,
        "similar_careers": similar
    }