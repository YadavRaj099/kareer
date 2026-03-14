def score_career(career, user_answers, rules):

weights = rules.get("weights", {})

score = 0

# -------------------------
# SAFE TAG EXTRACTION
# -------------------------

tags = career.get("tags", [])

if not isinstance(tags, list):
    tags = []

career_tags = [str(t).lower() for t in tags]

# -------------------------
# STREAM MATCH
# -------------------------

stream = user_answers.get("stream")

if stream and stream in career_tags:
    score += weights.get("stream", 2)

# -------------------------
# WORK STYLE
# -------------------------

work_style = user_answers.get("work_style")

if work_style and work_style in career_tags:
    score += weights.get("work_style", 2)

# -------------------------
# RISK TOLERANCE
# -------------------------

risk = user_answers.get("risk")

if risk and risk in career_tags:
    score += weights.get("risk", 1)

# -------------------------
# SKILLS MATCH
# -------------------------

skills = user_answers.get("skills", [])

for skill in skills:
    if skill in career_tags:
        score += weights.get("skills", 2)

# -------------------------
# INTEREST MATCH
# -------------------------

interests = user_answers.get("interests", [])

for interest in interests:
    if interest in career_tags:
        score += weights.get("interests", 2)

# -------------------------
# WORK ENVIRONMENT
# -------------------------

environment = user_answers.get("environment")

if environment and environment in career_tags:
    score += weights.get("environment", 1)

# -------------------------
# CAREER PRIORITY
# -------------------------

priority = user_answers.get("priority")

if priority and priority in career_tags:
    score += weights.get("priority", 1)

return score