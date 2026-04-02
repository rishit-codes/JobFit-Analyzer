import streamlit as st
from utils.extractor import extract_resume_text, scrape_jd_from_url
from utils.skills import get_combined_skills, generate_skill_gap_report, tag_skills
from utils.scoring import get_match_score, calculate_ats_score, generate_suggestions
from utils.report import generate_pdf_report
def main():
    st.set_page_config(page_title="Smart Job Description Analyzer", layout="centered")
    
    st.sidebar.markdown("### 🎯 Want a Human Expert Review?")
    st.sidebar.markdown(
        "Get a **personalized resume review** and **custom job targeting strategy** from me on Fiverr."
    )
    st.sidebar.markdown("[📦 Order on Fiverr →](https://www.fiverr.com/sellers/rishtz/edit)")
    st.sidebar.markdown("---")
    
    st.title("Smart Job Description Analyzer")
    st.write("Paste a job description and upload your resume to get an instant match score and skill gap report.")

    resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

    tab1, tab2 = st.tabs(["Single JD Analysis", "Multi-JD Compare"])
    
    with tab1:
        jd_input = st.text_area("Paste the Job Description or URL (LinkedIn/Internshala)", height=200, key="jd_single")
        
        if st.button("Analyze", key="analyze_single"):
            if jd_input and resume_file:
                with st.spinner("Analyzing..."):
                    try:
                        resume_text = extract_resume_text(resume_file)
                        jd_text = scrape_jd_from_url(jd_input.strip()) if jd_input.strip().startswith("http") else jd_input.strip()
                        
                        jd_skills = get_combined_skills(jd_text)
                        resume_skills = get_combined_skills(resume_text)
                        
                        score = get_match_score(jd_text, resume_text)
                        report = generate_skill_gap_report(jd_skills, resume_skills)
                        
                        ats_score = calculate_ats_score(jd_text, resume_text, report["missing"])
                        suggestions = generate_suggestions(report["missing"], resume_text)
                        
                        missing_skills_tagged = tag_skills(report["missing"])

                        st.subheader("Analysis Results")
                        
                        col_score1, col_score2 = st.columns(2)
                        col_score1.metric(label="Overall Match Score", value=f"{score}%")
                        col_score2.metric(label="ATS Compatibility Score", value=f"{ats_score}%")
                        
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
                            if missing_skills_tagged:
                                for skill in sorted(missing_skills_tagged):
                                    st.write(f"- {skill.title()}")
                            else:
                                st.write("No missing skills!")
                                
                        if suggestions:
                            st.subheader("💡 Tailored Resume Suggestions")
                            for s in suggestions:
                                st.info(s)
                                
                        st.subheader("📄 Download Report")
                        pdf_path = generate_pdf_report(score, report["matched"], report["missing"], suggestions)
                        with open(pdf_path, "rb") as f:
                            st.download_button(
                                label="Download PDF Report",
                                data=f,
                                file_name="jobfit_report.pdf",
                                mime="application/pdf"
                            )
                    except Exception as e:
                        st.error(f"An error occurred during analysis: {e}")
            else:
                st.warning("Please provide both a job description and a resume.")

    with tab2:
        st.write("Compare up to 3 Job Descriptions to see which one you match best.")
        jd1 = st.text_area("Job Description 1 (URL or Text)", key="jd1")
        jd2 = st.text_area("Job Description 2 (URL or Text)", key="jd2")
        jd3 = st.text_area("Job Description 3 (Optional)", key="jd3")
        
        if st.button("Compare All", key="compare_multi"):
            if resume_file and (jd1.strip() or jd2.strip() or jd3.strip()):
                with st.spinner("Comparing..."):
                    try:
                        resume_text = extract_resume_text(resume_file)
                        jds_raw = [jd1, jd2, jd3]
                        jds_processed = []
                        for i, jd_raw in enumerate(jds_raw):
                            val = jd_raw.strip()
                            if not val:
                                continue
                            text = scrape_jd_from_url(val) if val.startswith("http") else val
                            jds_processed.append((f"JD {i+1}", text))
                            
                        if not jds_processed:
                            st.warning("No valid JDs found to compare.")
                        else:
                            scores = []
                            for label, jd_t in jds_processed:
                                s = get_match_score(jd_t, resume_text)
                                scores.append((label, s))
                                
                            scores.sort(key=lambda x: x[1], reverse=True)
                            
                            st.subheader("🏆 Best Match Ranking")
                            for rank, (label, s) in enumerate(scores):
                                st.write(f"**{rank+1}. {label}** — {s}% match")
                    except Exception as e:
                        st.error(f"An error occurred during comparison: {e}")
            else:
                st.warning("Please upload a resume and provide at least one JD.")

if __name__ == "__main__":
    main()
