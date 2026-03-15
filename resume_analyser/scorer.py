# =====================================================
# RESUME SCORING ENGINE
# Compatible with Kareer Resume Analyzer Architecture
# =====================================================

from engine.resume_analyzer.role_skills import get_role_skills


# =====================================================
# SCORING CONFIGURATION
# Adjustable without touching algorithm
# =====================================================

SCORING_CONFIG = {

    "required_weight": 0.6,
    "optional_weight": 0.2,
    "tool_weight": 0.1,
    "soft_skill_weight": 0.1,
    "frequency_boost": 0.05

}


# =====================================================
# INTERVIEW PROBABILITY ESTIMATION
# =====================================================

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


# =====================================================
# READINESS CLASSIFICATION
# =====================================================

def classify_readiness(score):

    if score >= 80:
        return "Job Ready"

    if score >= 65:
        return "Almost Ready"

    if score >= 45:
        return "Needs Improvement"

    return "Beginner"


# =====================================================
# SAFE SET EXTRACTION
# =====================================================

def safe_set(data):

    if not data:
        return set()

    if isinstance(data, list):
        return set(data)

    return set()


# =====================================================
# MAIN SCORING FUNCTION
# =====================================================

def score_resume(extracted_skills, target_role):

    if not extracted_skills:

        return {
            "score": 0,
            "readiness": "Unknown",
            "interview_probability": "Unknown"
        }

    skills = set(extracted_skills.get("skills", []))

    frequency = extracted_skills.get("frequency", {})

    role_data = get_role_skills(target_role)

    if not role_data:

        return {

            "score": 0,
            "readiness": "Unknown Role",
            "interview_probability": "Unknown",
            "matched_skills": [],
            "missing_skills": [],
            "optional_skills_found": [],
            "tools_found": [],
            "soft_skills_found": []
        }

    required = safe_set(role_data.get("required"))
    optional = safe_set(role_data.get("optional"))
    tools = safe_set(role_data.get("tools"))
    soft = safe_set(role_data.get("soft_skills"))

    # -------------------------------------------------
    # MATCHING
    # -------------------------------------------------

    matched_required = skills.intersection(required)
    matched_optional = skills.intersection(optional)
    matched_tools = skills.intersection(tools)
    matched_soft = skills.intersection(soft)

    missing_required = required - skills

    # -------------------------------------------------
    # COVERAGE SCORES
    # -------------------------------------------------

    required_score = len(matched_required) / max(len(required), 1)
    optional_score = len(matched_optional) / max(len(optional), 1)
    tool_score = len(matched_tools) / max(len(tools), 1)
    soft_score = len(matched_soft) / max(len(soft), 1)

    # -------------------------------------------------
    # FREQUENCY BOOST
    # -------------------------------------------------

    freq_score = 0

    if frequency:

        total_mentions = sum(frequency.get(skill, 0) for skill in matched_required)

        freq_score = min(total_mentions / 10, 1)

    # -------------------------------------------------
    # FINAL SCORE
    # -------------------------------------------------

    total_score = (

        required_score * SCORING_CONFIG["required_weight"] +
        optional_score * SCORING_CONFIG["optional_weight"] +
        tool_score * SCORING_CONFIG["tool_weight"] +
        soft_score * SCORING_CONFIG["soft_skill_weight"]

    )

    total_score += freq_score * SCORING_CONFIG["frequency_boost"]

    percentage = round(min(total_score, 1) * 100)

    readiness = classify_readiness(percentage)

    interview_probability = estimate_interview_probability(percentage)

    # -------------------------------------------------
    # RETURN STRUCTURE
    # -------------------------------------------------

    return {

        "score": percentage,

        "readiness": readiness,

        "interview_probability": interview_probability,

        "matched_skills": sorted(list(matched_required)),

        "optional_skills_found": sorted(list(matched_optional)),

        "tools_found": sorted(list(matched_tools)),

        "soft_skills_found": sorted(list(matched_soft)),

        "missing_skills": sorted(list(missing_required)),

        "skill_gap": sorted(list(missing_required))

    }