def score_project(tags):
    score = 0

    if "ai" in tags:
        score += 4
    if "finance" in tags:
        score += 3
    if "web" in tags:
        score += 2

    return min(score, 10)