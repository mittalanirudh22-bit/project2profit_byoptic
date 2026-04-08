import json

with open("keywords.json") as f:
    KEYWORDS = json.load(f)

def analyze_project(description):
    description = description.lower()
    tags = []

    for category, words in KEYWORDS.items():
        for word in words:
            if word in description:
                tags.append(category)
                break

    complexity = "High" if len(tags) > 5 else "Medium" if len(tags) > 4 else "Low"

    return {"tags": tags, "complexity": complexity}