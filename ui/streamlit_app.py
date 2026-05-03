import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import requests

from app.resume_parser import (
    extract_text_from_pdf
)

# =========================================
# Page Config
# =========================================

st.set_page_config(
    page_title="Mini Jobright AI",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# Custom CSS
# =========================================

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.job-container {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    border: 1px solid #334155;
}

.skill-badge {
    display: inline-block;
    padding: 6px 12px;
    margin-right: 8px;
    margin-top: 8px;
    border-radius: 20px;
    background-color: #2563eb;
    color: white;
    font-size: 14px;
}

.apply-btn {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 10px;
    background-color: #22c55e;
    color: white !important;
    text-decoration: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# Backend URL
# =========================================

API_URL = (
    "https://mini-jobright-ai-production.up.railway.app/match"
)

# =========================================
# Header
# =========================================

st.title("🚀 Mini Jobright AI")

st.write(
    "AI-Powered Semantic Resume Matching Platform"
)

st.markdown("---")

# =========================================
# Upload Resume
# =========================================

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

resume_text = ""

# =========================================
# Extract Resume Text
# =========================================

if uploaded_file is not None:

    with st.spinner(
        "Extracting resume..."
    ):

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

    st.success(
        "Resume uploaded successfully!"
    )

    with st.expander(
        "📃 View Extracted Resume Text"
    ):

        st.text(
            resume_text[:5000]
        )

# =========================================
# Match Jobs
# =========================================

if st.button("🔍 Match Jobs"):

    if resume_text.strip() == "":

        st.warning(
            "Please upload a PDF resume."
        )

    else:

        try:

            with st.spinner(
                "Finding best jobs..."
            ):

                response = requests.post(
                    API_URL,
                    json={
                        "resume": resume_text
                    },
                    timeout=300
                )

                # =====================================
                # Debug Response
                # =====================================

                st.write(
                    "Status Code:",
                    response.status_code
                )

                # =====================================
                # Safe JSON Parsing
                # =====================================

                try:

                    data = response.json()

                except Exception:

                    st.error(
                        "Backend returned invalid JSON response"
                    )

                    st.text(response.text)

                    st.stop()

                # =====================================
                # Show Raw Response
                # =====================================

                st.write("Backend Response:")

                st.json(data)

                # =====================================
                # Safe Success Check
                # =====================================

                if data.get("success"):

                    st.subheader(
                        "🎯 Top Matching Jobs"
                    )

                    matches = data.get(
                        "matches",
                        []
                    )

                    if len(matches) == 0:

                        st.warning(
                            "No matching jobs found."
                        )

                    for match in matches:

                        # =====================================
                        # Safe Field Extraction
                        # =====================================

                        job_title = match.get(
                            "job_title",
                            "Unknown"
                        )

                        company = match.get(
                            "company",
                            "Unknown"
                        )

                        score = match.get(
                            "match_percentage",
                            0
                        )

                        reasoning = match.get(
                            "reasoning",
                            "No reasoning available"
                        )

                        location = match.get(
                            "location",
                            "Remote"
                        )

                        source = match.get(
                            "source",
                            "Unknown"
                        )

                        job_url = match.get(
                            "job_url",
                            ""
                        )

                        # =====================================
                        # Skill Extraction
                        # =====================================

                        skills = []

                        tech_keywords = [
                            "python",
                            "fastapi",
                            "machine learning",
                            "tensorflow",
                            "pytorch",
                            "react",
                            "sql",
                            "nlp",
                            "openai",
                            "langchain"
                        ]

                        lower_reasoning = (
                            reasoning.lower()
                        )

                        for tech in tech_keywords:

                            if tech in lower_reasoning:

                                skills.append(
                                    tech.title()
                                )

                        # =====================================
                        # Job Card
                        # =====================================

                        with st.container():

                            st.markdown(
                                '<div class="job-container">',
                                unsafe_allow_html=True
                            )

                            st.subheader(job_title)

                            st.write(
                                f"🏢 Company: {company}"
                            )

                            st.write(
                                f"🎯 Match Score: {score}%"
                            )

                            try:

                                st.progress(
                                    int(score)
                                )

                            except:

                                st.progress(0)

                            # =====================================
                            # Skill Badges
                            # =====================================

                            badge_html = ""

                            for skill in skills:

                                badge_html += f"""
                                <span class="skill-badge">
                                    {skill}
                                </span>
                                """

                            st.markdown(
                                badge_html,
                                unsafe_allow_html=True
                            )

                            st.write("")

                            # =====================================
                            # AI Analysis
                            # =====================================

                            with st.expander(
                                "🧠 View AI Analysis"
                            ):

                                st.write(reasoning)

                                st.write(
                                    f"📍 Location: {location}"
                                )

                                st.write(
                                    f"🌐 Source: {source}"
                                )

                            # =====================================
                            # Apply Button
                            # =====================================

                            if job_url:

                                st.markdown(
                                    f"""
                                    <a href="{job_url}"
                                    target="_blank"
                                    class="apply-btn">
                                    Apply Now
                                    </a>
                                    """,
                                    unsafe_allow_html=True
                                )

                            st.markdown(
                                "</div>",
                                unsafe_allow_html=True
                            )

                            st.markdown("---")

                else:

                    st.error(
                        data.get(
                            "error",
                            "Unknown backend error"
                        )
                    )

        except requests.exceptions.Timeout:

            st.error(
                "Request timeout. Backend is taking too long."
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to backend server."
            )

        except Exception as e:

            st.error(
                f"Frontend Error: {str(e)}"
            )