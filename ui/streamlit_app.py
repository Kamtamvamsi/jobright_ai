import streamlit as st
import requests

st.title("Mini Jobright AI")

resume_text = st.text_area("Paste Resume")

if st.button("Match Jobs"):

    response = requests.post(
        "http://127.0.0.1:8000/match",
        json={"resume": resume_text}
    )

    st.write("Status:", response.status_code)
    st.write("Response:", response.text)

    if response.status_code == 200:
        data = response.json()

        for match in data["matches"]:
            st.subheader(match["job_title"])
            st.write(match["reason"])
            # st.write("Score:", match["score"])
            st.write("Match Percentage:", match["match_percentage"], "%")

    else:
        st.error("Backend Error")