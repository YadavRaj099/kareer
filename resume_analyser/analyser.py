# =====================================================
# RESUME ANALYZER ORCHESTRATOR
# Production-ready pipeline manager
# =====================================================

from functools import lru_cache
from datetime import datetime

from engine.resume_analyzer.parser import parse_resume
from engine.resume_analyzer.skill_extractor import extract_skills
from engine.resume_analyzer.resume_scorer import score_resume
from engine.resume_analyzer.role_skills import (
    get_role_skills,
    list_available_roles
)


# =====================================================
# MAIN ANALYSIS PIPELINE
# =====================================================

def analyze_resume(uploaded_file, target_role):

    analysis = {

        "timestamp": datetime.utcnow().isoformat(),

        "target_role": target_role,

        "resume_text": "",

        "skills": {},

        "score": {},

        "career_recommendations": [],

        "analysis_metrics": {}

    }

    try:

        # ------------------------------------------------
        # STEP 1 — PARSE RESUME
        # ------------------------------------------------

        resume_text = parse_resume(uploaded_file)

        analysis["resume_text"] = resume_text


        # ------------------------------------------------
        # STEP 2 — SKILL EXTRACTION
        # ------------------------------------------------

        extracted_skills = extract_skills(resume_text)

        analysis["skills"] = extracted_skills


        # ------------------------------------------------
        # STEP 3 — ROLE VALIDATION
        # ------------------------------------------------

        role_data = get_role_skills(target_role)

        if not role_data:

            analysis["score"] = {
                "score": 0,
                "readiness": "Unknown Role",
                "interview_probability": "Unknown"
            }

        else:

            # ---------------------------------------------
            # STEP 4 — RESUME SCORING
            # ---------------------------------------------

            scoring = score_resume(extracted_skills, target_role)

            analysis["score"] = scoring


        # ------------------------------------------------
        # STEP 5 — CAREER RECOMMENDATION
        # ------------------------------------------------

        analysis["career_recommendations"] = recommend_roles(extracted_skills)


        # ------------------------------------------------
        # STEP 6 — ANALYTICS
        # ------------------------------------------------

        analysis["analysis_metrics"] = generate_metrics(
            resume_text,
            extracted_skills
        )


    except Exception as e:

        print("Resume Analyzer Error:", e)

    return analysis


# =====================================================
# ROLE RECOMMENDATION ENGINE
# =====================================================

def recommend_roles(extracted_skills, top_n=5):

    skills = set(extracted_skills.get("skills", []))

    roles = list_available_roles()

    ranking = []

    for role in roles:

        role_data = get_role_skills(role)

        if not role_data:
            continue

        required = set(role_data.get("required", []))
        optional = set(role_data.get("optional", []))

        score = len(skills.intersection(required)) * 3
        score += len(skills.intersection(optional))

        ranking.append((role, score))

    ranking.sort(key=lambda x: x[1], reverse=True)

    return [r[0] for r in ranking[:top_n]]


# =====================================================
# ANALYSIS METRICS
# Extra intelligence layer
# =====================================================

def generate_metrics(resume_text, extracted_skills):

    words = resume_text.split()

    total_words = len(words)

    skills_found = extracted_skills.get("skill_count", 0)

    skill_density = 0

    if total_words > 0:

        skill_density = round((skills_found / total_words) * 100, 2)

    return {

        "resume_length_words": total_words,

        "skills_detected": skills_found,

        "skill_density_percent": skill_density

    }


# =====================================================
# SUMMARY GENERATOR
# UI-ready insights
# =====================================================

def generate_summary(analysis):

    score = analysis.get("score", {})

    skills = analysis.get("skills", {})

    metrics = analysis.get("analysis_metrics", {})

    return {

        "resume_score": score.get("score", 0),

        "readiness": score.get("readiness", "Unknown"),

        "interview_probability": score.get(
            "interview_probability",
            "Unknown"
        ),

        "skills_detected": skills.get("skill_count", 0),

        "resume_length": metrics.get("resume_length_words", 0),

        "skill_density": metrics.get("skill_density_percent", 0),

        "missing_skills": score.get("missing_skills", []),

        "recommended_roles": analysis.get(
            "career_recommendations",
            []
        )
    }


# =====================================================
# BULK ROLE ANALYSIS
# Useful for career discovery mode
# =====================================================

def analyze_all_roles(uploaded_file):

    resume_text = parse_resume(uploaded_file)

    extracted = extract_skills(resume_text)

    roles = list_available_roles()

    results = []

    for role in roles:

        scoring = score_resume(extracted, role)

        results.append({

            "role": role,

            "score": scoring.get("score", 0)

        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:10]