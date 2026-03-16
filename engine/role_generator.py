import json
import copy
from pathlib import Path


# =====================================================
# PATHS
# =====================================================

DATA_PATH = Path("data/roles_database.json")


# =====================================================
# BASE ROLE TEMPLATES
# =====================================================

templates = {

    "data_role": {
        "required": ["python", "statistics", "data analysis"],
        "optional": ["machine learning", "sql", "pandas"],
        "tools": ["jupyter", "excel"],
        "soft_skills": ["problem solving", "communication"],
        "experience_keywords": ["analytics", "data modelling"]
    },

    "developer_role": {
        "required": ["programming", "algorithms", "databases"],
        "optional": ["api", "cloud", "docker"],
        "tools": ["git", "linux"],
        "soft_skills": ["problem solving", "teamwork"],
        "experience_keywords": ["software development"]
    },

    "design_role": {
        "required": ["design principles", "ui", "ux"],
        "optional": ["figma", "prototyping"],
        "tools": ["figma", "adobe xd"],
        "soft_skills": ["creativity", "communication"],
        "experience_keywords": ["product design"]
    },

    "business_role": {
        "required": ["analysis", "strategy", "communication"],
        "optional": ["excel", "presentation"],
        "tools": ["excel", "notion"],
        "soft_skills": ["leadership", "communication"],
        "experience_keywords": ["business operations"]
    }
}


# =====================================================
# ROLE CATEGORIES
# =====================================================

role_categories = {

    "data": [
        "data_scientist",
        "data_analyst",
        "data_engineer",
        "machine_learning_engineer",
        "ai_engineer",
        "analytics_engineer",
        "business_intelligence_analyst"
    ],

    "developer": [
        "backend_developer",
        "frontend_developer",
        "full_stack_developer",
        "software_engineer",
        "devops_engineer",
        "cloud_engineer",
        "mobile_app_developer",
        "game_developer",
        "blockchain_developer",
        "systems_engineer",
        "database_administrator",
        "network_engineer"
    ],

    "design": [
        "ui_designer",
        "ux_designer",
        "product_designer",
        "graphic_designer",
        "motion_designer",
        "brand_designer"
    ],

    "business": [
        "product_manager",
        "project_manager",
        "business_analyst",
        "operations_manager",
        "marketing_manager",
        "growth_manager",
        "seo_specialist",
        "content_strategist",
        "sales_manager"
    ]
}


# =====================================================
# LOAD EXISTING DATABASE
# =====================================================

def load_existing():

    if DATA_PATH.exists():

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    return {}


# =====================================================
# VALIDATE ROLE STRUCTURE
# =====================================================

def validate_role(role_data):

    required_fields = [
        "required",
        "optional",
        "tools",
        "soft_skills",
        "experience_keywords"
    ]

    for field in required_fields:

        if field not in role_data:
            return False

        if not isinstance(role_data[field], list):
            return False

    return True


# =====================================================
# GENERATE ROLES
# =====================================================

def generate_roles():

    database = load_existing()

    created = 0

    for category, roles in role_categories.items():

        if category == "data":
            template = templates["data_role"]

        elif category == "developer":
            template = templates["developer_role"]

        elif category == "design":
            template = templates["design_role"]

        else:
            template = templates["business_role"]

        for role in roles:

            if role not in database:

                role_data = copy.deepcopy(template)

                if validate_role(role_data):

                    database[role] = role_data
                    created += 1

    return database, created


# =====================================================
# SAVE DATABASE
# =====================================================

def save_database(db):

    DATA_PATH.parent.mkdir(exist_ok=True)

    with open(DATA_PATH, "w", encoding="utf-8") as f:

        json.dump(db, f, indent=2)


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    database, created = generate_roles()

    save_database(database)

    print("Roles database generated successfully")
    print("New roles added:", created)
    print("Total roles:", len(database))