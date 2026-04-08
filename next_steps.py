def generate_next_steps(tags):
    steps = []

    if "web" in tags:
        steps.append("Build MVP using Streamlit or Flask")
    if "ai" in tags:
        steps.append("Train ML model using sklearn")

    steps.append("Launch on LinkedIn")
    steps.append("Get first users")

    return steps