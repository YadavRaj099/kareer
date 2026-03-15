import re
from collections import defaultdict


# ======================================================
# SKILL DATABASE (Expandable)
# ======================================================

SKILL_DB = {

    "programming": [
        "python","java","c","c++","c#","javascript","typescript","go","rust","kotlin","swift"
    ],

    "data_science": [
        "machine learning","deep learning","data science","data analysis",
        "tensorflow","pytorch","scikit learn","pandas","numpy","statistics"
    ],

    "web_development": [
        "html","css","react","nextjs","nodejs","express","django","flask",
        "rest api","graphql","frontend","backend","full stack"
    ],

    "cloud_devops": [
        "aws","azure","gcp","google cloud","docker","kubernetes",
        "devops","ci cd","cloud computing","terraform"
    ],

    "database": [
        "sql","mysql","postgresql","mongodb","redis","database design"
    ],

    "design": [
        "ui design","ux design","figma","photoshop","illustrator","adobe xd"
    ],

    "business": [
        "marketing","sales","strategy","product management","market research"
    ],

    "soft_skills": [
        "communication","leadership","teamwork","problem solving",
        "critical thinking","time management"
    ]

}


# ======================================================
# SYNONYMS / ABBREVIATIONS
# ======================================================

ALIASES = {

    "js": "javascript",
    "ml": "machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence",
    "node": "nodejs",
    "reactjs": "react",
    "postgres": "postgresql",
    "gcloud": "google cloud"
}


# ======================================================
# NORMALIZE TEXT
# ======================================================

def normalize(text):

    text = text.lower()

    text = re.sub(r"[^a-z0-9\+\#\.\-\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ======================================================
# TOKENIZE TEXT
# ======================================================

def tokenize(text):

    tokens = text.split()

    return tokens


# ======================================================
# BUILD MASTER SKILL SET
# ======================================================

def build_skill_index():

    skill_index = {}

    for category, skills in SKILL_DB.items():

        for skill in skills:

            skill_index[skill] = category

    return skill_index


SKILL_INDEX = build_skill_index()


# ======================================================
# APPLY ALIASES
# ======================================================

def apply_aliases(tokens):

    mapped = []

    for t in tokens:

        if t in ALIASES:
            mapped.append(ALIASES[t])

        mapped.append(t)

    return mapped


# ======================================================
# SKILL EXTRACTION ENGINE
# ======================================================

def extract_skills(resume_text):

    if not resume_text:

        return {
            "skills": [],
            "categories": {},
            "skill_count": 0,
            "frequency": {}
        }

    text = normalize(resume_text)

    tokens = tokenize(text)

    tokens = apply_aliases(tokens)

    detected = set()

    frequency = defaultdict(int)

    categories = defaultdict(list)

    # ---------------------------------------
    # TOKEN LEVEL DETECTION
    # ---------------------------------------

    for token in tokens:

        if token in SKILL_INDEX:

            detected.add(token)

            frequency[token] += 1

            category = SKILL_INDEX[token]

            if token not in categories[category]:

                categories[category].append(token)


    # ---------------------------------------
    # PHRASE LEVEL DETECTION
    # ---------------------------------------

    for skill, category in SKILL_INDEX.items():

        if " " in skill:

            if skill in text:

                detected.add(skill)

                frequency[skill] += 1

                if skill not in categories[category]:

                    categories[category].append(skill)


    # ---------------------------------------
    # FINAL STRUCTURE
    # ---------------------------------------

    result = {

        "skills": sorted(list(detected)),

        "categories": dict(categories),

        "frequency": dict(frequency),

        "skill_count": len(detected)

    }

    return result