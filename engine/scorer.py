def score_career(career, user_answers, rules):

    weights = rules.get("weights", {})

    score = 0

    # Safe tags extraction
    tags = career.get("tags", [])

    if not isinstance(tags, list):
        tags = []

    career_tags = [str(t).lower() for t in tags]

    # STREAM MATCH
    if user_answers.get("stream") in career_tags:
        score += weights.get("stream", 1)

    # WORK STYLE
    if user_answers.get("work_style") in career_tags:
        score += weights.get("work_style", 1)

    # RISK
    if user_answers.get("risk") in career_tags:
        score += weights.get("risk", 1)

    # SKILLS
    for skill in user_answers.get("skills", []):
        if skill in career_tags:
            score += weights.get("skills", 1)

    return score