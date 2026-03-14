def score_career(career, user_answers, rules):

    if not isinstance(career, dict):
        return 0

    weights = rules.get("weights", {})

    score = 0

    tags = career.get("tags", [])

    if not isinstance(tags, list):
        tags = []

    career_tags = [str(t).lower() for t in tags]

    stream = user_answers.get("stream")
    if stream and stream in career_tags:
        score += weights.get("stream", 2)

    work_style = user_answers.get("work_style")
    if work_style and work_style in career_tags:
        score += weights.get("work_style", 2)

    risk = user_answers.get("risk")
    if risk and risk in career_tags:
        score += weights.get("risk", 1)

    skills = user_answers.get("skills", [])
    for skill in skills:
        if skill in career_tags:
            score += weights.get("skills", 2)

    interests = user_answers.get("interests", [])
    for interest in interests:
        if interest in career_tags:
            score += weights.get("interests", 2)

    environment = user_answers.get("environment")
    if environment and environment in career_tags:
        score += weights.get("environment", 1)

    priority = user_answers.get("priority")
    if priority and priority in career_tags:
        score += weights.get("priority", 1)

    return score