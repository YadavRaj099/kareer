def score_career(career, user, rules):

    weights = rules["weights"]

    score = 0
    max_score = sum(weights.values())

    career_tags = [t.lower() for t in career.get("tags", [])]

    # SUBJECT MATCH
    user_subjects = [s.lower() for s in user.get("subjects", [])]

    if any(sub in career_tags for sub in user_subjects):
        score += weights["subjects_match"]

    # INTEREST MATCH
    interest = user.get("work_type", "").lower()

    if interest in career_tags:
        score += weights["interest_match"]

    # WORK STYLE
    team_style = user.get("team_style", "").lower()

    if team_style in career_tags:
        score += weights["work_style_match"]

    # RISK MATCH
    career_risk = career.get("risk", "").lower()
    user_risk = user.get("risk", "").lower()

    if career_risk == user_risk:
        score += weights["risk_match"]

    # EDUCATION YEARS
    education_pref = user.get("education_commitment", "")

    if education_pref == career.get("education_years"):
        score += weights["education_match"]

    # MOTIVATION
    motivation = user.get("motivation", "").lower()

    if motivation in career_tags:
        score += weights["motivation_match"]

    # LIFESTYLE
    lifestyle = user.get("lifestyle", "").lower()

    if lifestyle in career_tags:
        score += weights["lifestyle_match"]

    percentage = round((score / max_score) * 100, 2)

    return percentage