def suggest_monetization(tags):
    ideas = []

    if "ai" in tags:
        ideas.append("SaaS Subscription")
    if "web" in tags:
        ideas.append("Freelance Service")
    if "finance" in tags:
        ideas.append("Premium Analytics Tool")

    if not ideas:
        ideas.append("Sell as Digital Product")

    return ideas