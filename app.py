import streamlit as st
import pdfplumber
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="HireSense by Aparna", layout="wide")
st.title("HireSense by Aparna 🧠")
st.write("Upload your resume and paste a job description to see how well you match.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")
    uploaded_file = st.file_uploader("Upload Resume PDF", type="pdf")
    resume_text = ""
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                resume_text += page.extract_text() or ""
        st.success("Resume uploaded successfully!")

with col2:
    st.subheader("Job Description")
    job_description = st.text_area("Paste the Job Description here", height=300)

if st.button("Analyze Match", type="primary"):
    if not resume_text or not job_description:
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("HireSense AI is analyzing..."):
            import time
            import random
            time.sleep(2) # fake AI thinking time
            
            # Smart fake logic based on keywords
            resume_lower = resume_text.lower()
            jd_lower = job_description.lower()
            
            skills_to_check = ["python", "sql", "fastapi", "docker", "aws", "git", "pandas", "react", "django"]
            matching = [skill for skill in skills_to_check if skill in resume_lower and skill in jd_lower]
            missing = [skill for skill in skills_to_check if skill in jd_lower and skill not in resume_lower]
            
            score = min(95, 40 + len(matching) * 12 - len(missing) * 5)
            verdict = "Strong Match" if score > 80 else "Good Fit" if score > 60 else "Weak Match"
            
            st.subheader("Analysis Result")
            st.metric("Match Score", f"{score}%")
            st.write("**Top Matching Skills:**", ", ".join(matching[:3]) if matching else "None detected")
            st.write("**Missing Skills:**", ", ".join(missing[:3]) if missing else "None detected")
            st.write("**Verdict:**", verdict)
            st.write("**Justification:**", f"Found {len(matching)} key skills in both. Focus on gaining experience in: {', '.join(missing[:2])}" if missing else "Strong alignment across all key areas.")
            st.caption("Demo Mode: Using rule-based matching. Add OpenAI credits for real AI analysis.")