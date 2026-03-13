from engine.loader import load_json
from engine.scorer import score_career

def recommend(user_answers):

    careers = load_json("data/careers.json")
    rules = load_json("data/scoring_rules.json")

    results = []

    for career in careers:

        score = score_career(career, user_answers, rules)

        results.append({
            "career": career.get("name"),
            "score": score,
            "data": career
        })

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    return ranked[:5]