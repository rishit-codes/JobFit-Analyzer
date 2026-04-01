# Smart Job Description Analyzer — Phased Build Plan

> Paste a job description, upload your resume, get an instant match score and skill gap report.

---

## Phase 1 — Foundation & Text Pipeline (Days 1–2)

**Goal:** Get raw text flowing in from both inputs — the JD and the resume.

### Tasks
- [ ] Set up project structure (`app.py`, `requirements.txt`, `utils/`)
- [ ] Create a virtual environment and install core dependencies
- [ ] Implement **PDF text extraction** using `pdfplumber`
- [ ] Accept **job description** as plain text input
- [ ] Write unit tests to verify clean text output from both sources

### Key Code

```python
import pdfplumber

def extract_resume_text(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return " ".join(page.extract_text() or "" for page in pdf.pages)
```

### Exit Criteria
✅ Given any PDF resume, the function returns a clean text string.
✅ JD text is captured from a simple text input.

---

## Phase 2 — Skill Extraction Engine (Days 3–4)

**Goal:** Identify and compare skills from both the JD and the resume.

### Tasks
- [ ] Build a curated skill list (~50–100 common tech skills)
- [ ] Implement **keyword-based skill matching** (v1 — simple & fast)
- [ ] Layer in **spaCy NER** for smarter entity recognition (v2 — optional enhancement)
- [ ] Generate the skill gap report: ✅ matched skills vs ❌ missing skills
- [ ] Test with 3–5 real JD + resume pairs

### Key Code

```python
SKILLS = ["python", "react", "sql", "docker", "machine learning", "nlp",
          "tensorflow", "aws", "git", "pandas", "flask", "api", "linux"]

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill in text_lower]
```

### Exit Criteria
✅ Skill extraction works on both JD and resume text.
✅ Matched and missing skills are correctly identified.

---

## Phase 3 — Semantic Similarity & Scoring (Day 5)

**Goal:** Produce a meaningful match percentage using NLP embeddings.

### Tasks
- [ ] Integrate `sentence-transformers` with the `all-MiniLM-L6-v2` model
- [ ] Encode JD and resume into vector embeddings
- [ ] Compute **cosine similarity** and convert to a percentage score
- [ ] Combine the similarity score with the skill gap data into a final report

### Key Code

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_match_score(jd_text, resume_text):
    embeddings = model.encode([jd_text, resume_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 1)
```

### Exit Criteria
✅ Match score is produced as a percentage (0–100%).
✅ Score feels reasonable across different JD/resume combos.

---

## Phase 4 — Streamlit UI & Integration (Day 6)

**Goal:** Wire everything together into a clean, usable web interface.

### Tasks
- [ ] Build the Streamlit layout: text area (JD), file uploader (resume), analyze button
- [ ] Display **match score** as a prominent metric
- [ ] Show **skills matched** (✅) and **skills missing** (❌) in styled sections
- [ ] Add suggestions: "What to highlight" / "What to learn next"
- [ ] Polish UI — add title, description, spacing, and visual hierarchy

### Key Code

```python
import streamlit as st

st.title("Smart Job Description Analyzer")

jd = st.text_area("Paste the job description")
resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if st.button("Analyze") and jd and resume_file:
    resume_text = extract_resume_text(resume_file)
    score = get_match_score(jd, resume_text)
    jd_skills = extract_skills(jd)
    resume_skills = extract_skills(resume_text)

    st.metric("Match Score", f"{score}%")
    st.success("Skills you have: " + ", ".join(set(jd_skills) & set(resume_skills)))
    st.error("Skills you're missing: " + ", ".join(set(jd_skills) - set(resume_skills)))
```

### Exit Criteria
✅ App runs locally with `streamlit run app.py`.
✅ Full pipeline works end-to-end: paste JD → upload PDF → see results.

---

## Phase 5 — Deployment & Presentation (Day 7)

**Goal:** Ship the app live and make it portfolio-ready.

### Tasks
- [ ] Create a Hugging Face account and a new **Streamlit Space**
- [ ] Upload `app.py` and `requirements.txt` to the Space
- [ ] Verify the app is live and publicly accessible
- [ ] Write a polished **GitHub README** (problem, tech, demo link, how to run locally)
- [ ] Draft a short **LinkedIn post** with the live link and the story behind it
- [ ] Add the live link to portfolio / Fiverr / internship applications

### Deployment Steps

```bash
# 1. Install dependencies locally
pip install streamlit pdfplumber sentence-transformers scikit-learn spacy
python -m spacy download en_core_web_sm

# 2. Deploy to Hugging Face Spaces
#    - Create a Space at huggingface.co → choose Streamlit SDK
#    - Upload app.py + requirements.txt
#    - Live at: https://huggingface.co/spaces/<username>/<app-name>
```

### The Story Angle
> You built this because you were struggling to find internships yourself.
> That's authentic and relatable — lead with it in every post and cold message.

### Exit Criteria
✅ App is live on Hugging Face Spaces with a shareable public URL.
✅ GitHub repo has a clean README with the demo link.

---

## Dependencies

```txt
streamlit
pdfplumber
sentence-transformers
scikit-learn
spacy
```

---

## Phase Summary

| Phase | Focus | Days | Deliverable |
|-------|-------|------|-------------|
| 1 | Foundation & Text Pipeline | 1–2 | Clean text extraction from JD + resume |
| 2 | Skill Extraction Engine | 3–4 | Skill matching & gap report |
| 3 | Semantic Similarity | 5 | NLP-based match score |
| 4 | UI & Integration | 6 | Working Streamlit app |
| 5 | Deploy & Present | 7 | Live app + portfolio pieces |
