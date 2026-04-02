---
title: JobFitAnalyzer
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: AI-powered resume & job description matcher.
---

# Smart Job Description Analyzer `v2.0` 🚀

> **Upgrade v2:** Now with ATS Scoring, PDF Reports, and Multi-JD Comparison.
> A professional-grade tool to boost your job search credibility.

🌐 **Live Demo:** [Hugging Face Space Link Here](#)

## 💡 Key Features (v2)

1. **ATS Score Simulation:** Get an "ATS Compatibility" score that checks keyword density, formatting red flags, and file hygiene.
2. **Downloadable PDF Reports:** Export your full analysis (match score, matched/missing skills, and suggestions) as a clean, shareable PDF.
3. **Multi-JD Comparison:** Paste up to 3 job descriptions to see which role you match best, ranked by score.
4. **URL Scraping:** Paste a job posting URL (LinkedIn, Internshala, etc.) instead of copying text manually.
5. **Tailored Resume Suggestions:** Actionable coaching on where to add missing skills in your resume.
6. **Skill Trend Badges:** See which of your missing skills are `🔥 Trending` or `⚡ In Demand` in the current market.

## 🛠️ Tech Stack

- **Python:** Core backend logic.
- **Streamlit:** Fast and interactive UI.
- **pdfplumber:** Robust PDF parsing for resume text.
- **fpdf2:** Professional PDF report generation.
- **spaCy:** NLP for dynamic skill entity recognition.
- **sentence-transformers:** Semantic similarity scoring using `all-MiniLM-L6-v2`.
- **BeautifulSoup4 & Requests:** Web scraping for JD URLs.
- **scikit-learn:** Cosine similarity calculation.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd JobFit
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## 🤝 Contribution
Feel free to fork this project, submit PRs, or use it to build your own ML portfolio.
