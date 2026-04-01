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

# Smart Job Description Analyzer

> A portfolio ML/AI project: paste a job description, upload your resume, get an instant match score and skill gap report.

🌐 **Live Demo:** [Hugging Face Space Link Here](#) *(Replace with your actual HF Spaces link after deployment)*

## 💡 What It Does

Finding the right job match is tough. This tool makes it easier by instantly analyzing your resume against any job description. 

1. **Paste a job description** (from LinkedIn, specialized boards, or company careers pages).
2. **Upload your resume** (PDF format).
3. **Get Insights**:
   - **Match Score:** A percentage of how well your resume contextually fits the JD.
   - **Skills You Have:** What matched perfectly.
   - **Skills You're Missing:** The gaps you need to fill to become the perfect candidate.

## 🛠️ Tech Stack

- **Python:** Core backend logic.
- **Streamlit:** Fast and interactive UI.
- **pdfplumber:** Robust PDF parsing to extract clean resume text.
- **spaCy:** NLP for smarter, dynamic skill entity recognition.
- **sentence-transformers:** `all-MiniLM-L6-v2` model for deep semantic similarity scoring and embedding generation.
- **scikit-learn:** Cosine similarity calculation to generate the final match percentage.

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
