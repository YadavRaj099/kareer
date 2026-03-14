def score_career(career, user_answers, rules):

    if not isinstance(career, dict):
        return 0

    weights = rules.get("weights", {})

    score = 0

    # -----------------------------
    # SAFE TAG EXTRACTION
    # -----------------------------

    tags = career.get("tags", [])

    if not isinstance(tags, list):
        tags = []

    career_tags = [str(t).lower() for t in tags]

    # -----------------------------
    # HELPER FUNCTION
    # -----------------------------

    def match(value, weight):

        nonlocal score

        if not value:
            return

        value = str(value).lower()

        # exact match
        if value in career_tags:
            score += weight
            return

        # partial match
        for tag in career_tags:
            if value in tag or tag in value:
                score += weight * 0.6
                return

    # -----------------------------
    # STREAM
    # -----------------------------

    match(user_answers.get("stream"), weights.get("stream", 3))

    # -----------------------------
    # WORK STYLE
    # -----------------------------

    match(user_answers.get("work_style"), weights.get("work_style", 3))

    # -----------------------------
    # RISK
    # -----------------------------

    match(user_answers.get("risk"), weights.get("risk", 2))

    # -----------------------------
    # ENVIRONMENT
    # -----------------------------

    match(user_answers.get("environment"), weights.get("environment", 2))

    # -----------------------------
    # PRIORITY
    # -----------------------------

    match(user_answers.get("priority"), weights.get("priority", 2))

    # -----------------------------
    # SKILLS
    # -----------------------------

    skills = user_answers.get("skills", [])

    if isinstance(skills, list):

        for skill in skills:

            skill = str(skill).lower()

            if skill in career_tags:
                score += weights.get("skills", 3)

            else:
                for tag in career_tags:
                    if skill in tag or tag in skill:
                        score += weights.get("skills", 3) * 0.5
                        break

    # -----------------------------
    # INTERESTS
    # -----------------------------

    interests = user_answers.get("interests", [])

    if isinstance(interests, list):

        for interest in interests:

            interest = str(interest).lower()

            if interest in career_tags:
                score += weights.get("interests", 3)

            else:
                for tag in career_tags:
                    if interest in tag or tag in interest:
                        score += weights.get("interests", 3) * 0.5
                        break

    # -----------------------------
    # FINAL SCORE SAFETY
    # -----------------------------

    if score == 0:
        score = 1

    return round(score, 2)