def calculate_similarity(career_a, career_b):

    tags_a = set([t.lower() for t in career_a.get("tags", [])])
    tags_b = set([t.lower() for t in career_b.get("tags", [])])

    if not tags_a or not tags_b:
        return 0

    shared_tags = tags_a.intersection(tags_b)
    total_tags = tags_a.union(tags_b)

    similarity_score = len(shared_tags) / len(total_tags)

    return similarity_score


def find_similar_careers(target_career, careers, threshold=0.4, max_results=5):

    similar = []

    for career in careers:

        if career["name"] == target_career["name"]:
            continue

        similarity = calculate_similarity(target_career, career)

        if similarity >= threshold:

            similar.append({
                "career": career["name"],
                "similarity": round(similarity,2),
                "data": career
            })

    similar_sorted = sorted(similar, key=lambda x: x["similarity"], reverse=True)

    return similar_sorted[:max_results]