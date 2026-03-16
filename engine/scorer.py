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

    if not career_tags:
        return 0

    # -----------------------------
    # HELPER FUNCTION
    # -----------------------------

    def match(value, weight):

        nonlocal score

        if not value:
            return

        value = str(value).lower()

        # Exact match
        if value in career_tags:
            score += weight
            return

        # Partial match (reduced impact)
        for tag in career_tags:
            if value in tag or tag in value:
                score += weight * 0.4
                return

    # -----------------------------
    # STREAM
    # -----------------------------

    match(user_answers.get("stream"), weights.get("stream", 4))

    # -----------------------------
    # WORK STYLE
    # -----------------------------

    match(user_answers.get("work_style"), weights.get("work_style", 3))

    # -----------------------------
    # RISK
    # -----------------------------

    match(user_answers.get("risk"), weights.get("risk", 1))

    # -----------------------------
    # ENVIRONMENT
    # -----------------------------

    match(user_answers.get("environment"), weights.get("environment", 2))

    # -----------------------------
    # PRIORITY
    # -----------------------------

    match(user_answers.get("career_priority"), weights.get("priority", 2))

    # -----------------------------
    # SKILLS
    # -----------------------------

    skills = user_answers.get("skills", [])

    if isinstance(skills, list):

        skill_hits = 0

        for skill in skills:

            skill = str(skill).lower()

            if skill in career_tags:
                score += weights.get("skills", 3)
                skill_hits += 1

            else:
                for tag in career_tags:
                    if skill in tag or tag in skill:
                        score += weights.get("skills", 3) * 0.4
                        skill_hits += 1
                        break

            # Prevent skill spam
            if skill_hits >= 3:
                break

    # -----------------------------
    # INTERESTS
    # -----------------------------

    interests = user_answers.get("interests", [])

    if isinstance(interests, list):

        interest_hits = 0

        for interest in interests:

            interest = str(interest).lower()

            if interest in career_tags:
                score += weights.get("interests", 3)
                interest_hits += 1

            else:
                for tag in career_tags:
                    if interest in tag or tag in interest:
                        score += weights.get("interests", 3) * 0.4
                        interest_hits += 1
                        break

            # Prevent inflation
            if interest_hits >= 3:
                break

    # -----------------------------
    # NORMALIZATION
    # -----------------------------

    tag_factor = max(1, len(career_tags))

    normalized_score = score / (tag_factor ** 0.3)

    return round(normalized_score, 2)