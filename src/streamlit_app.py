import streamlit as st
from utils.extractor import extract_resume_text
from utils.skills import get_combined_skills, generate_skill_gap_report
from utils.scoring import get_match_score

def main():
    st.set_page_config(page_title="Smart Job Description Analyzer", layout="centered")
    
    st.title("Smart Job Description Analyzer")
    st.write("Paste a job description and upload your resume to get an instant match score and skill gap report.")

    jd_text = st.text_area("Paste the Job Description Here", height=200)
    resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

    if st.button("Analyze"):
        if jd_text and resume_file:
            with st.spinner("Analyzing..."):
                try:
                    # 1. Extract Text
                    resume_text = extract_resume_text(resume_file)
                    
                    # 2. Extract Skills
                    jd_skills = get_combined_skills(jd_text)
                    resume_skills = get_combined_skills(resume_text)
                    
                    # 3. Calculate Score
                    score = get_match_score(jd_text, resume_text)
                    
                    # 4. Generate Gap Report
                    report = generate_skill_gap_report(jd_skills, resume_skills)

                    # Display Results
                    st.subheader("Analysis Results")
                    st.metric(label="Overall Match Score", value=f"{score}%")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.success("✅ Skills You Have")
                        if report["matched"]:
                            for skill in sorted(report["matched"]):
                                st.write(f"- {skill.title()}")
                        else:
                            st.write("No matching skills found.")
                            
                    with col2:
                        st.error("❌ Skills You're Missing")
                        if report["missing"]:
                            for skill in sorted(report["missing"]):
                                st.write(f"- {skill.title()}")
                        else:
                            st.write("No missing skills!")
                            
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
        else:
            st.warning("Please provide both a job description and a resume.")

if __name__ == "__main__":
    main()
