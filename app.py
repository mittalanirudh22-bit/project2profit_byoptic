import streamlit as st
from analyser import analyze_project
from moneytizer import suggest_monetization
from scorer import score_project
from next_steps import generate_next_steps
from database import save_project, load_projects

st.set_page_config(page_title="Project2Profit", layout="centered")

st.title("🚀 Project2Profit")
st.subheader("Turn your ideas into income 💰")

menu = st.sidebar.selectbox("Menu", ["Submit Project", "Marketplace"])

# ---------------- SUBMIT ----------------
if menu == "Submit Project":
    st.header("📌 Submit Your Project")

    description = st.text_area("Describe your project")

    if st.button("Analyze"):
        analysis = analyze_project(description)
        monetization = suggest_monetization(analysis["tags"])
        score = score_project(analysis["tags"])
        steps = generate_next_steps(analysis["tags"])

        project_data = {
            "description": description,
            "tags": analysis["tags"],
            "score": score,
            "monetization": monetization
        }

        save_project(project_data)

        st.success("Analysis Complete!")

        st.write("### 📊 Analysis")
        st.write("Tags:", analysis["tags"])
        st.write("Complexity:", analysis["complexity"])
        st.write("Score:", score, "/10")

        st.write("### 💰 Monetization")
        for m in monetization:
            st.write("-", m)

        st.write("### 🚀 Next Steps")
        for s in steps:
            st.write("-", s)

# ---------------- MARKETPLACE ----------------
elif menu == "Marketplace":
    st.header("🛒 Marketplace")

    projects = load_projects()

    if not projects:
        st.warning("No projects yet. Submit one first!")
    else:
        for p in projects:
            st.subheader("📌 Project")
            st.write("Description:", p["description"])
            st.write("Tags:", p["tags"])
            st.write("Score:", p["score"])
            st.write("Monetization:", p["monetization"])
            st.markdown("---")