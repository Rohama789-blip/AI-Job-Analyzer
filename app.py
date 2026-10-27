
import json
import html

import streamlit as st
from graph import job_analysis_graph


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HireLens AI | Job Analyzer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #0b1020;
    color: #edf0ff;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(11,16,32,0.95);
}

[data-testid="stSidebar"] {
    background: #10172a;
    border-right: 1px solid #26304a;
}

[data-testid="stSidebar"] * {
    color: #e3e9ff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(125deg, #171e3b, #252052 65%, #192d50);
    border: 1px solid #34365f;
    margin-bottom: 28px;
}

.eyebrow {
    color: #a5a0ff;
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 800;
}

.hero h1 {
    color: #ffffff;
    font-size: clamp(28px, 4vw, 42px);
    line-height: 1.2;
    margin: 12px 0;
    font-weight: 800;
}

.hero p {
    color: #c2c9e4;
    font-size: 15px;
    margin-bottom: 0;
}

.section-title {
    font-size: 21px;
    font-weight: 750;
    color: #f3f5ff;
    margin: 26px 0 14px;
}

.metric-card {
    background: linear-gradient(145deg, #151d32, #12192b);
    border: 1px solid #2a3651;
    border-radius: 17px;
    padding: 20px;
    min-height: 135px;
    margin-bottom: 10px;
}

.metric-label {
    color: #9ca9c9;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.metric-value {
    color: #ffffff;
    font-size: 19px;
    font-weight: 750;
    overflow-wrap: anywhere;
}

.metric-icon {
    font-size: 22px;
    margin-bottom: 12px;
}

.panel {
    background: #121a2d;
    border: 1px solid #293550;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 16px;
}

.panel-title {
    font-size: 18px;
    font-weight: 750;
    color: #f2f4ff;
    margin-bottom: 8px;
}

.panel-subtitle {
    color: #929fbd;
    font-size: 13px;
    margin-bottom: 18px;
}

.skill-tag {
    display: inline-block;
    background: #222447;
    border: 1px solid #44427a;
    color: #c9c6ff;
    border-radius: 9px;
    padding: 8px 12px;
    margin: 4px 5px 4px 0;
    font-size: 12px;
    font-weight: 600;
    overflow-wrap: anywhere;
}

.top-skill {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #192238;
    border: 1px solid #303b56;
    padding: 14px;
    border-radius: 12px;
    margin-top: 10px;
}

.skill-number {
    color: #a8a0ff;
    font-size: 20px;
    font-weight: 800;
}

.skill-name {
    color: #f4f5ff;
    font-size: 15px;
    font-weight: 650;
}

.footer {
    color: #7987a8;
    text-align: center;
    font-size: 12px;
    padding: 30px 0 10px;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #7165f4, #9a60ee);
    color: white;
    border: none;
    border-radius: 11px;
    padding: 0.72rem 1rem;
    font-weight: 750;
    min-height: 48px;
    transition: 0.2s ease;
}

div.stButton > button[kind="primary"]:hover {
    border: 1px solid #c0b7ff;
    filter: brightness(1.1);
}

div.stDownloadButton > button {
    background: #202b44;
    color: #e8ecff;
    border: 1px solid #465577;
    border-radius: 10px;
    min-height: 44px;
    font-weight: 650;
}

div.stDownloadButton > button:hover {
    border-color: #a59bff;
    color: white;
}

.stTextArea textarea {
    background: #10182a;
    color: #edf0ff;
    border: 1px solid #354260;
    border-radius: 12px;
    line-height: 1.7;
}

.stTextArea textarea:focus {
    border-color: #8b7bff;
}

[data-testid="stExpander"] {
    background: #121a2d;
    border: 1px solid #293550;
    border-radius: 12px;
}

hr {
    border-color: #26324b;
}

@media (max-width: 768px) {
    .hero {
        padding: 22px;
    }
    .metric-card {
        padding: 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- HELPERS ----------------
def render_metric(icon, label, value):
    safe_value = html.escape(str(value or "Not specified"))
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{safe_value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel(title, subtitle, skills):
    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)

    tags = "".join(
        f'<span class="skill-tag">{html.escape(str(skill))}</span>'
        for skill in skills
    )

    if not tags:
        tags = '<span style="color:#929fbd">No skills identified.</span>'

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">{safe_title}</div>
            <div class="panel-subtitle">{safe_subtitle}</div>
            {tags}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_top_skills(skills):
    st.markdown(
        '<div class="panel-title">⭐ Top 3 Skills</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="panel-subtitle">Most important skills identified by AI</div>',
        unsafe_allow_html=True,
    )

    if not skills:
        st.info("No top skills identified.")
        return

    for index, skill in enumerate(skills[:3], start=1):
        st.markdown(
            f"""
            <div class="top-skill">
                <div class="skill-number">{index:02}</div>
                <div class="skill-name">{html.escape(str(skill))}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💼 HireLens AI")
    st.caption("INTELLIGENT HIRING ASSISTANT")
    st.markdown("---")

    st.markdown("### Navigation")
    st.markdown("🔎  Job Analyzer")
    st.markdown("📊  Hiring Insights")
    st.markdown("📁  JSON Reports")

    st.markdown("---")
    st.markdown("### Technology")
    st.caption("🐍 Python")
    st.caption("🔗 LangGraph")
    st.caption("⚡ Groq API")
    st.caption("🧩 Pydantic")
    st.caption("🎨 Streamlit")

    st.markdown("---")
    st.caption("AI-powered job description analysis")


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ AI-POWERED RECRUITMENT</div>
    <h1>Job Description Analyzer</h1>
    <p>
        Transform job postings into structured hiring insights.
        Extract requirements, classify roles, and discover essential skills.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT ----------------
st.markdown(
    '<div class="section-title">01 &nbsp; Job Description</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="panel-subtitle">Paste the complete job description below to get started.</div>',
    unsafe_allow_html=True,
)

job_description = st.text_area(
    "Job description",
    height=220,
    label_visibility="collapsed",
    placeholder=(
        "Example: We are looking for a Python AI Engineer with 2+ years "
        "of experience in Python, LangGraph, FastAPI and REST APIs. "
        "Strong problem-solving and communication skills are required. "
        "This is a full-time, on-site position."
    ),
)

col_button, col_hint = st.columns([1, 2])

with col_button:
    analyze_button = st.button(
        "✦  Analyze Job Description",
        type="primary",
        use_container_width=True,
    )

with col_hint:
    st.caption("Powered by LangGraph + Groq • Structured AI analysis")


# ---------------- ANALYSIS ----------------
if analyze_button:
    if not job_description.strip():
        st.warning("Please paste a job description first.")

    elif len(job_description.strip()) < 30:
        st.warning(
            "Please enter a more detailed job description "
            "with at least 30 characters."
        )

    else:
        try:
            with st.spinner(
                "Analyzing job requirements, classifying the role, "
                "and extracting skills..."
            ):
                result = job_analysis_graph.invoke(
                    {"job_description": job_description.strip()}
                )

            report = result.get("hiring_report")

            if not isinstance(report, dict):
                raise ValueError(
                    "The workflow did not return a valid hiring report."
                )

            # Store result for viewing after Streamlit reruns
            st.session_state["hiring_report"] = report
            st.session_state["analyzed_description"] = job_description

            st.success("Analysis completed successfully!")

        except Exception as error:
            st.error(
                "Analysis failed. Check your Groq API key, model, "
                "internet connection, and terminal error."
            )
            with st.expander("Technical error details"):
                st.code(str(error))


# ---------------- REPORT ----------------
report = st.session_state.get("hiring_report")

if report:
    st.markdown("---")
    st.markdown(
        '<div class="section-title">02 &nbsp; Hiring Overview</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric(
            "💼",
            "Job Title",
            report.get("job_title", "Not specified"),
        )

    with c2:
        render_metric(
            "🧠",
            "Job Category",
            report.get("job_category", "Not specified"),
        )

    with c3:
        render_metric(
            "⏳",
            "Experience",
            report.get("required_experience", "Not specified"),
        )

    with c4:
        render_metric(
            "📍",
            "Employment Type",
            report.get("employment_type", "Not specified"),
        )

    # Company details
    st.markdown(
        '<div class="section-title">03 &nbsp; Position Details</div>',
        unsafe_allow_html=True,
    )

    company = html.escape(
        str(report.get("company_name", "Not specified"))
    )

    st.markdown(
        f"""
        <div class="panel">
            <div class="metric-label">COMPANY</div>
            <div class="metric-value">{company}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        render_panel(
            "🛠️ Required Skills",
            "Skills mentioned in the job requirements",
            report.get("required_skills", []),
        )

        render_panel(
            "💻 Technical Skills",
            "Tools, technologies, and technical capabilities",
            report.get("technical_skills", []),
        )

    with right:
        render_panel(
            "🤝 Soft Skills",
            "Communication, collaboration, and other people skills",
            report.get("soft_skills", []),
        )

        st.markdown('<div class="panel">', unsafe_allow_html=True)
        render_top_skills(report.get("top_3_skills", []))
        st.markdown("</div>", unsafe_allow_html=True)

    # Export report
    st.markdown("---")
    st.markdown(
        '<div class="section-title">04 &nbsp; Export Report</div>',
        unsafe_allow_html=True,
    )

    json_data = json.dumps(
        report,
        indent=4,
        ensure_ascii=False,
    )

    download_col, preview_col = st.columns([1, 1])

    with download_col:
        st.download_button(
            "⬇️  Download Hiring Report (JSON)",
            data=json_data,
            file_name="hiring_report.json",
            mime="application/json",
            use_container_width=True,
        )

    with preview_col:
        with st.expander("View raw JSON"):
            st.json(report)

    st.markdown(
        '<div class="footer">SmartHire AI • Built with Python, LangGraph, Groq & Streamlit</div>',
        unsafe_allow_html=True,
    )
