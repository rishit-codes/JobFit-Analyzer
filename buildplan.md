# Smart Job Description Analyzer — Full Build Plan

> A portfolio ML/AI project: paste a job description, upload your resume, get an instant match score and skill gap report.

---

## Overview

| Detail | Info |
|--------|------|
| Time to build | ~1 week |
| Difficulty | Beginner–Intermediate |
| Deployment | Hugging Face Spaces (free) |
| Stack | Python, Streamlit, HuggingFace |

---

## What It Does — User Flow

1. **Paste a job description** — user copies any JD from LinkedIn, Internshala, or a company careers page and pastes it into a text box.
2. **Upload resume** — user uploads their resume as a PDF. The app extracts raw text automatically.
3. **App outputs:**
   - Match score (e.g. 72%)
   - Skills you have ✅
   - Skills you're missing ❌
   - What to highlight / learn next

---

## Tech Stack

| Part | Tool | Why |
|------|------|-----|
| Language | Python | Core language for all ML logic |
| PDF reading | pdfplumber | Extracts clean text from uploaded PDFs |
| Skill extraction | spaCy | NER + keyword matching on JD text |
| NLP / embeddings | sentence-transformers | Converts text to semantic embeddings |
| Similarity scoring | Cosine similarity | Measures closeness between resume and JD |
| UI | Streamlit | Instant Python UI, no frontend needed |
| Deployment | Hugging Face Spaces | Free hosting, shareable public link |

**Recommended model:** `all-MiniLM-L6-v2` — fast, free, accurate enough for this use case.

---

## Build It in 4 Steps

### Step 1 — Extract Text (~1 day)

- Accept job description as plain text input
- Accept resume as PDF upload
- Use `pdfplumber` to extract clean text from the PDF

**Goal:** two clean strings — one for the JD, one for the resume — ready to pass into the next step.

```python
import pdfplumber

def extract_resume_text(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages)
```

---

### Step 2 — Skill Extraction (~2 days)

- Build a predefined skill list (Python, React, SQL, Docker, TensorFlow, etc.)
- Use simple keyword matching first — get it working, then improve
- Optionally layer in `spaCy` for smarter NER

**Tip:** Start with ~50–100 common tech skills. You can expand the list later.

```python
SKILLS = ["python", "react", "sql", "docker", "machine learning", "nlp", "tensorflow"]

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill in text_lower]
```

---

### Step 3 — Similarity Scoring (~2 days)

- Convert the JD and resume into embeddings using `sentence-transformers`
- Calculate cosine similarity and turn it into a percentage match score

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_match_score(jd_text, resume_text):
    embeddings = model.encode([jd_text, resume_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 1)
```

---

### Step 4 — UI + Deploy (~1 day)

- Build a clean Streamlit interface with two inputs and a results panel
- Deploy on Hugging Face Spaces — you get a public shareable link instantly

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

---

## 7-Day Timeline

| Day | Focus |
|-----|-------|
| Day 1 | PDF + text extraction setup |
| Day 2 | Skill list + keyword matching |
| Day 3 | spaCy NLP integration |
| Day 4 | Embeddings + cosine similarity |
| Day 5 | Match score + gap report logic |
| Day 6 | Streamlit UI polish |
| Day 7 | Deploy on HF Spaces + share |

---

## How to Present It

### GitHub README
Write what the project does, what problem it solves, what tech you used, and how to run it locally. Always link to the live Hugging Face demo at the top.

### LinkedIn Post
> "Built a tool that tells you how well your resume matches any job description — here's how I made it."

Short story, live link, what you learned. Even 150 words works.

### Fiverr / Portfolio
Add the live Hugging Face link as a sample work piece. A working AI app is far stronger than listing skills with no proof.

### The Story Angle
You built this because you were struggling to find internships yourself. That's authentic and relatable — lead with it in every post and cold message. Buyers and recruiters respond to real motivation.

---

## Dependencies

```txt
streamlit
pdfplumber
sentence-transformers
scikit-learn
spacy
```

Install with:
```bash
pip install streamlit pdfplumber sentence-transformers scikit-learn spacy
python -m spacy download en_core_web_sm
```

---

## Deployment (Hugging Face Spaces)

1. Create a free account at [huggingface.co](https://huggingface.co)
2. Create a new Space → choose **Streamlit** as the SDK
3. Upload your files (`app.py`, `requirements.txt`)
4. Your app goes live at `https://huggingface.co/spaces/your-username/your-app-name`
5. Share this link everywhere — GitHub, LinkedIn, Fiverr, internship applications
