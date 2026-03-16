# =====================================================
# ROLE SKILLS LOGIC ENGINE
# Future-proof role skill manager
# =====================================================

import json
from functools import lru_cache


# =====================================================
# DATABASE LOCATION
# =====================================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROLE_DB_PATH = BASE_DIR / "data" / "roles_database.json"


# =====================================================
# LOAD DATABASE
# =====================================================

@lru_cache(maxsize=1)
def load_role_database():
    """
    Load role database from JSON file.
    Cached to avoid repeated disk reads.
    """

    try:

        with open(ROLE_DB_PATH, "r", encoding="utf-8") as f:

            data = json.load(f)

            if isinstance(data, dict):
                return data

    except Exception as e:

        print("Role database loading error:", e)

    return {}


# =====================================================
# NORMALIZE ROLE NAME
# =====================================================

def normalize_role(role):
    """
    Normalize role name for consistent lookup
    """

    if not role:
        return None

    role = role.lower().strip()

    role = role.replace(" ", "_")

    return role


# =====================================================
# GET ROLE SKILLS
# =====================================================

def get_role_skills(role):
    """
    Retrieve full skill structure for a role
    """

    db = load_role_database()

    role = normalize_role(role)

    return db.get(role)


# =====================================================
# LIST AVAILABLE ROLES
# =====================================================

def list_available_roles():
    """
    Return all roles supported by the system
    """

    db = load_role_database()

    return sorted(list(db.keys()))


# =====================================================
# SEARCH ROLES BY SKILL
# =====================================================

def find_roles_by_skill(skill):
    """
    Return roles that require a given skill
    """

    db = load_role_database()

    skill = skill.lower()

    roles = []

    for role, data in db.items():

        required = data.get("required", [])
        optional = data.get("optional", [])

        if skill in required or skill in optional:
            roles.append(role)

    return roles


# =====================================================
# VALIDATE ROLE STRUCTURE
# =====================================================

def validate_role_structure(role_data):
    """
    Ensure role data follows correct schema
    """

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
# ADD ROLE (future expansion support)
# =====================================================

def add_role(role_name, role_data):
    """
    Dynamically add new roles (for admin tools)
    """

    db = load_role_database()

    role = normalize_role(role_name)

    if not validate_role_structure(role_data):

        raise ValueError("Invalid role schema")

    db[role] = role_data

    return db


# =====================================================
# ROLE STATISTICS
# =====================================================

def role_statistics():
    """
    Provide insights about role database
    """

    db = load_role_database()

    total_roles = len(db)

    total_skills = 0

    for role in db.values():

        total_skills += len(role.get("required", []))
        total_skills += len(role.get("optional", []))

    return {
        "roles_supported": total_roles,
        "total_skills_defined": total_skills
    }