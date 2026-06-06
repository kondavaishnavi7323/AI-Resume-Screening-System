import streamlit as st
import PyPDF2

st.title("AI Resume Screening System")

required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Data Analysis"
]

uploaded_file = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    score = 0
    found_skills = []

    for skill in required_skills:

        if skill.lower() in text.lower():

            score += 25
            found_skills.append(skill)

    st.write("Skills Found:")
    st.write(found_skills)

    st.write("Resume Score:", score, "/100")

    if score >= 75:
        st.success("Excellent Resume")

    elif score >= 50:
        st.warning("Good Resume")

    else:
        st.error("Needs Improvement")