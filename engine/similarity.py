def find_similar_careers(best_career, careers):

    if not isinstance(best_career, dict):
        return []

    best_tags = best_career.get("tags", [])

    if not isinstance(best_tags, list):
        best_tags = []

    best_tags = [str(t).lower() for t in best_tags]

    similar = []

    for career in careers:

        if not isinstance(career, dict):
            continue

        tags = career.get("tags", [])

        if not isinstance(tags, list):
            continue

        tags = [str(t).lower() for t in tags]

        common = set(best_tags) & set(tags)

        if len(common) >= 2:
            similar.append(career.get("name", "Unknown"))

    return similar[:5]