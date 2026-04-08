import streamlit as st
import pandas as pd
from analyser import analyze_project
from moneytizer import suggest_monetization
from scorer import score_project
from next_steps import generate_next_steps
from database import save_project, load_projects

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Project2Profit", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: white;
}
.stButton>button {
    background-color: #ef4444;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 Project2Profit")
st.caption("Turn your ideas into income 💰")

menu = st.sidebar.radio("Navigation", ["Submit Project", "Marketplace"])

# ---------------- SUBMIT ----------------
if menu == "Submit Project":

    st.header("📌 Submit Your Project")

    description = st.text_area("Describe your project", height=150)

    if st.button("Analyze 🚀"):

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

        st.success("✅ Analysis Complete!")

        col1, col2 = st.columns(2)

        # ---------------- ANALYSIS ----------------
        with col1:
            st.subheader("📊 Analysis")

            st.metric("Score", f"{score}/10")
            st.write("**Tags:**", analysis["tags"])
            st.write("**Complexity:**", analysis["complexity"])

            # Chart
            df = pd.DataFrame({
                "Metric": ["Score"],
                "Value": [score]
            })

            st.bar_chart(df.set_index("Metric"))

        # ---------------- MONETIZATION ----------------
        with col2:
            st.subheader("💰 Monetization Ideas")

            for m in monetization:
                st.success(m)

        # ---------------- NEXT STEPS ----------------
        st.subheader("🚀 Next Steps")

        for i, step in enumerate(steps, 1):
            st.write(f"{i}. {step}")

# ---------------- MARKETPLACE ----------------
elif menu == "Marketplace":

    st.header("🛒 Marketplace")

    projects = load_projects()

    if not projects:
        st.warning("No projects yet. Submit one first!")
    else:
        for p in projects:

            with st.container():
                st.markdown("### 📌 Project")

                col1, col2 = st.columns([3,1])

                with col1:
                    st.write("**Description:**", p["description"])
                    st.write("**Tags:**", ", ".join(p["tags"]))
                    st.write("**Monetization:**", ", ".join(p["monetization"]))

                with col2:
                    st.metric("Score", f"{p['score']}/10")

                st.markdown("---")