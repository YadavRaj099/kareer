from engine.loader import load_json
from engine.scorer import score_career
from engine.similarity import find_similar_careers


CAREERS_FILE = "data/careers.json"
RULES_FILE = "data/scoring_rules.json"


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
# CLASSIFY MATCH STRENGTH
# -----------------------------------

def classify(score, rules):

    thresholds = rules.get("classification", {})

    perfect = thresholds.get("perfect", 12)
    strong = thresholds.get("strong", 9)
    alt = thresholds.get("alternative", 6)
    weak = thresholds.get("weak", 3)

    if score >= perfect:
        return "Perfect Match"

    elif score >= strong:
        return "Strong Match"

    elif score >= alt:
        return "Alternative"

    elif score >= weak:
        return "Weak Match"

    return "Exploratory Match"


# -----------------------------------
# CONFIDENCE SCORE
# -----------------------------------

def confidence(score, max_score=20):

    if max_score == 0:
        return 50

    pct = (score / max_score) * 100

    pct = max(45, min(95, pct))

    return round(pct)


# -----------------------------------
# NORMALIZE USER ANSWERS
# -----------------------------------

def normalize_answers(user_answers):

    clean = {}

    for k, v in user_answers.items():

        if isinstance(v, list):
            clean[k] = [str(x).lower() for x in v]

        else:
            clean[k] = str(v).lower()

    return clean


# -----------------------------------
# GENERATE EXPLANATION
# -----------------------------------

def explain_match(career, user_answers):

    explanation = []

    tags = career.get("tags", [])
    tags = [str(t).lower() for t in tags]

    stream = user_answers.get("stream")

    if stream and stream in tags:
        explanation.append("Your academic stream aligns well with this career.")

    skills = user_answers.get("skills", [])

    for skill in skills:
        if skill in tags:
            explanation.append(f"Your skill in {skill.replace('_',' ')} supports this path.")
            break

    interests = user_answers.get("interests", [])

    for interest in interests:
        if interest in tags:
            explanation.append(f"Your interest in {interest.replace('_',' ')} matches this field.")
            break

    work_style = user_answers.get("work_style")

    if work_style and work_style in tags:
        explanation.append("Your preferred work style fits this career.")

    if not explanation:
        explanation.append("Your responses show potential alignment with this field.")

    return explanation


# -----------------------------------
# WEIGHTED SCORE ADJUSTMENT
# -----------------------------------

def adjust_score(base_score, career, user_answers):

    tags = [str(t).lower() for t in career.get("tags", [])]

    bonus = 0

    # STREAM MATCH
    stream = user_answers.get("stream")
    if stream and stream in tags:
        bonus += 3

    # INTEREST MATCH
    interests = user_answers.get("interests", [])
    for i in interests:
        if i in tags:
            bonus += 1

    # SKILL MATCH
    skills = user_answers.get("skills", [])
    for s in skills:
        if s in tags:
            bonus += 1

    # WORK STYLE
    work_style = user_answers.get("work_style")
    if work_style and work_style in tags:
        bonus += 2

    return base_score + bonus


# -----------------------------------
# REMOVE VERY SIMILAR CAREERS
# -----------------------------------

def diversify(results, limit=5):

    selected = []
    seen_tags = set()

    for r in results:

        tags = tuple(sorted(r["data"].get("tags", [])))

        if tags in seen_tags:
            continue

        selected.append(r)
        seen_tags.add(tags)

        if len(selected) >= limit:
            break

    return selected


# -----------------------------------
# MAIN RECOMMENDATION ENGINE
# -----------------------------------

def recommend(user_answers, top_n=5):

    careers = load_careers()
    rules = load_json(RULES_FILE)

    user_answers = normalize_answers(user_answers)

    results = []

    # ----------------------------
    # SCORE ALL CAREERS
    # ----------------------------

    for career in careers:

        if not isinstance(career, dict):
            continue

        base_score = score_career(career, user_answers, rules)

        score = adjust_score(base_score, career, user_answers)

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

    if not ranked:
        return {
            "matches": [],
            "similar_careers": []
        }

    # ----------------------------
    # DIVERSIFY RESULTS
    # ----------------------------

    top_results = diversify(ranked, top_n)

    # ----------------------------
    # FIND SIMILAR CAREERS
    # ----------------------------

    best_career = top_results[0].get("data", {})

    try:
        similar = find_similar_careers(best_career, careers)
    except Exception:
        similar = []

    if not similar and len(ranked) > 3:
        similar = [r["data"] for r in ranked[3:6]]

    return {
        "matches": top_results,
        "similar_careers": similar
    }