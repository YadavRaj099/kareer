from engine.resume_analyzer.role_skills import ROLE_SKILLS


# ---------------------------------------------------
# CONFIGURATION
# Adjust weights without touching logic
# ---------------------------------------------------

SCORING_CONFIG = {

    "required_weight": 0.7,
    "optional_weight": 0.2,
    "frequency_weight": 0.1

}


# ---------------------------------------------------
# INTERVIEW PROBABILITY ESTIMATION
# ---------------------------------------------------

def estimate_interview_probability(score):

    if score >= 85:
        return "Very High"

    if score >= 70:
        return "High"

    if score >= 55:
        return "Moderate"

    if score >= 40:
        return "Low"

    return "Very Low"


# ---------------------------------------------------
# READINESS CLASSIFICATION
# ---------------------------------------------------

def classify_readiness(score):

    if score >= 80:
        return "Job Ready"

    if score >= 65:
        return "Almost Ready"

    if score >= 45:
        return "Needs Improvement"

    return "Beginner"


# ---------------------------------------------------
# MAIN SCORING ENGINE
# ---------------------------------------------------

def score_resume(extracted_skills, target_role):

    if not extracted_skills:
        return {}

    skills = set(extracted_skills.get("skills", []))
    frequency = extracted_skills.get("frequency", {})

    role_data = ROLE_SKILLS.get(target_role)

    if not role_data:

        return {

            "score": 0,
            "readiness": "Unknown Role",
            "interview_probability": "Unknown",
            "matched_skills": [],
            "missing_skills": [],
            "optional_skills_found": [],
            "skill_gap": []
        }

    required = set(role_data.get("required", []))
    optional = set(role_data.get("optional", []))

    # ------------------------------------------
    # MATCHING
    # ------------------------------------------

    matched_required = skills.intersection(required)
    matched_optional = skills.intersection(optional)

    missing_required = required - skills

    # ------------------------------------------
    # REQUIRED SCORE
    # ------------------------------------------

    required_score = len(matched_required) / max(len(required), 1)

    # ------------------------------------------
    # OPTIONAL SCORE
    # ------------------------------------------

    optional_score = len(matched_optional) / max(len(optional), 1)

    # ------------------------------------------
    # FREQUENCY BOOST
    # ------------------------------------------

    freq_score = 0

    if frequency:

        freq_total = sum(frequency.get(skill, 0) for skill in matched_required)

        freq_score = min(freq_total / 10, 1)

    # ------------------------------------------
    # FINAL SCORE
    # ------------------------------------------

    total_score = (

        required_score * SCORING_CONFIG["required_weight"] +
        optional_score * SCORING_CONFIG["optional_weight"] +
        freq_score * SCORING_CONFIG["frequency_weight"]

    )

    percentage = round(total_score * 100)

    readiness = classify_readiness(percentage)

    interview_probability = estimate_interview_probability(percentage)

    return {

        "score": percentage,

        "readiness": readiness,

        "interview_probability": interview_probability,

        "matched_skills": sorted(list(matched_required)),

        "optional_skills_found": sorted(list(matched_optional)),

        "missing_skills": sorted(list(missing_required)),

        "skill_gap": sorted(list(missing_required))

    }