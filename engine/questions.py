def get_questions():

    return {

        "stream": {
            "question": "Which broad academic field interests you the most?",
            "type": "single",
            "options": {
                "Science, Technology & Engineering": "stem",
                "Business, Finance & Entrepreneurship": "business",
                "Creative Arts, Design & Media": "creative",
                "Social Sciences & Psychology": "social_sciences",
                "Healthcare & Medical Sciences": "healthcare",
                "Law, Policy & Government": "law_policy"
            }
        },

        "subjects": {
            "question": "Which subjects do you enjoy studying the most?",
            "type": "multi",
            "options": {
                "Mathematics": "math",
                "Biology": "biology",
                "Computer Science": "programming",
                "Economics / Business Studies": "finance",
                "Psychology": "psychology",
                "Design / Art": "design",
                "Environmental Science": "environment"
            }
        },

        "interests": {
            "question": "Which areas genuinely interest you?",
            "type": "multi",
            "options": {
                "Technology and innovation": "technology",
                "Finance and markets": "finance",
                "Medicine and healthcare": "medicine",
                "Design and creativity": "design",
                "Human behavior and psychology": "psychology",
                "Business and startups": "business",
                "Scientific research": "research",
                "Education and teaching": "education",
                "Environment and sustainability": "environment",
                "Media and storytelling": "media"
            }
        },

        "skills": {
            "question": "Which skills do you enjoy using or developing?",
            "type": "multi",
            "options": {
                "Mathematics and logical reasoning": "math",
                "Programming or technology building": "programming",
                "Problem solving": "problem_solving",
                "Communication and presentation": "communication",
                "Creative thinking": "creativity",
                "Biology or medical knowledge": "biology",
                "Writing and storytelling": "writing",
                "Data analysis": "data_analysis",
                "Leadership": "leadership",
                "Negotiation or persuasion": "negotiation"
            }
        },

        "work_style": {
            "question": "What type of work sounds most exciting to you?",
            "type": "single",
            "options": {
                "Analyzing complex problems": "analytical",
                "Designing creative solutions": "creative",
                "Helping people directly": "helping_people",
                "Building products or technology": "building_products",
                "Managing people or projects": "managing_teams",
                "Exploring research questions": "researching"
            }
        },

        "thinking_style": {
            "question": "How would you describe your thinking style?",
            "type": "single",
            "options": {
                "Highly analytical and logical": "analytical",
                "Creative and imaginative": "creative",
                "Empathetic and people-focused": "people_oriented",
                "Strategic and leadership oriented": "leadership"
            }
        },

        "risk": {
            "question": "How comfortable are you with career risk?",
            "type": "single",
            "options": {
                "Prefer stability and security": "low",
                "Balanced between stability and opportunity": "medium",
                "Comfortable with uncertainty and risk": "high"
            }
        },

        "environment": {
            "question": "What work environment suits you best?",
            "type": "single",
            "options": {
                "Corporate office": "office",
                "Remote or flexible work": "remote",
                "Scientific laboratory": "laboratory",
                "Outdoor or field work": "outdoor",
                "Dynamic startup environment": "startup"
            }
        },

        "impact": {
            "question": "What type of impact motivates you the most?",
            "type": "single",
            "options": {
                "Building innovative technology": "innovation",
                "Helping people directly": "helping_people",
                "Growing wealth or businesses": "financial_growth",
                "Creative expression": "creative_expression",
                "Advancing science or knowledge": "scientific_discovery"
            }
        },

        "education_commitment": {
            "question": "How many years are you willing to study for your career?",
            "type": "single",
            "options": {
                "3–4 years": "short_term",
                "5–6 years": "medium_term",
                "7–10+ years": "long_term"
            }
        },

        "work_preference": {
            "question": "Which type of tasks do you prefer most?",
            "type": "single",
            "options": {
                "Solving complex problems": "solving_complex_problems",
                "Creating new ideas or products": "creating_new_things",
                "Organizing people and systems": "organizing_people",
                "Analyzing data and patterns": "analyzing_data",
                "Teaching or guiding others": "teaching_or_guiding"
            }
        },

        "leadership_interest": {
            "question": "Do you enjoy leading or organizing people?",
            "type": "single",
            "options": {
                "Yes, I enjoy leadership roles": "leadership",
                "Sometimes": "moderate_leadership",
                "Not particularly": "low_leadership"
            }
        },

        "technology_interest": {
            "question": "How interested are you in technology?",
            "type": "single",
            "options": {
                "Very interested": "high_tech",
                "Somewhat interested": "medium_tech",
                "Not very interested": "low_tech"
            }
        },

        "science_interest": {
            "question": "How interested are you in scientific research?",
            "type": "single",
            "options": {
                "Very interested": "high_science",
                "Somewhat interested": "medium_science",
                "Not interested": "low_science"
            }
        },

        "lifestyle": {
            "question": "What type of lifestyle do you want from your career?",
            "type": "single",
            "options": {
                "Stable work-life balance": "stable",
                "High income even if stressful": "high_income",
                "Creative and flexible lifestyle": "creative_life",
                "Prestigious or influential career": "prestige"
            }
        },

        "career_priority": {
            "question": "What matters most to you in a career?",
            "type": "single",
            "options": {
                "High salary": "salary",
                "Job stability": "stability",
                "Creativity": "creativity",
                "Making an impact": "impact",
                "Freedom and independence": "freedom"
            }
        }

    }