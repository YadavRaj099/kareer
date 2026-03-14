def find_similar_careers(target, careers, limit=3):

target_tags = set(target.get("tags", []))

similar = []

for career in careers:

    if not isinstance(career, dict):
        continue

    if career.get("name") == target.get("name"):
        continue

    tags = set(career.get("tags", []))

    overlap = len(target_tags & tags)

    if overlap > 0:
        similar.append((career.get("name"), overlap))

similar_sorted = sorted(similar, key=lambda x: x[1], reverse=True)

return [name for name, _ in similar_sorted[:limit]]