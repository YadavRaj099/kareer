def score_career(career, user, rules):

    score = 0

    tags = career.get("tags", [])
    risk = career.get("risk", "")

    if user["subjects"].lower() in [t.lower() for t in tags]:
        score += rules["subjects_match"]

    if user["work_type"].lower() in [t.lower() for t in tags]:
        score += rules["work_type_match"]

    if user["risk"].lower() == risk.lower():
        score += rules["risk_match"]

    return score