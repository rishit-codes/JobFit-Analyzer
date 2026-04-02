import spacy
from typing import List, Set

# Attempt to load the spaCy English model.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If not found, fallback or download logic (handled externally, but good practice to catch)
    nlp = None

# A predefined list of common technical and professional skills.
# This list can be extensively expanded in the future.
CURATED_SKILLS = [
    "python", "java", "c++", "c#", "javascript", "typescript", "ruby", "go", "php", "swift", "kotlin",
    "html", "css", "react", "angular", "vue", "node.js", "django", "flask", "spring", "express",
    "sql", "mysql", "postgresql", "mongodb", "redis", "cassandra", "sqlite",
    "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible", "jenkins", "git", "github", "gitlab",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
    "data science", "data analysis", "agile", "scrum", "kanban", "devops", "ci/cd",
    "streamlit", "tableau", "power bi", "excel", "linux", "bash", "powershell",
    "rest", "graphql", "grpc", "microservices"
]

def extract_skills_keyword(text: str) -> List[str]:
    """
    Extracts skills by looking for exact keyword matches (case-insensitive).
    """
    if not text:
        return []
    text_lower = text.lower()
    return [skill for skill in CURATED_SKILLS if skill in text_lower]

def extract_skills_spacy(text: str) -> List[str]:
    """
    Uses spaCy NER and noun chunks to identify potential unnamed skills implicitly or dynamically.
    For this basic implementation, we will merge keyword checking with NER entities (ORG, PRODUCT).
    """
    if not text or not nlp:
        return []
        
    doc = nlp(text)
    extracted = set()
    
    # Check exact noun chunks against our curated list (handles some misspellings optionally, but mostly dynamic parsing)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.lower().strip()
        if chunk_text in CURATED_SKILLS:
            extracted.add(chunk_text)
            
    # Also grab known entities that might be frameworks/tools labeled as ORG or PRODUCT
    for ent in doc.ents:
        ent_text = ent.text.lower().strip()
        if ent.label_ in ["ORG", "PRODUCT"] and ent_text in CURATED_SKILLS:
            extracted.add(ent_text)
            
    return list(extracted)

def get_combined_skills(text: str) -> List[str]:
    """
    Combines both keyword matching and spaCy extraction for robustness.
    """
    keywords = set(extract_skills_keyword(text))
    spacy_skills = set(extract_skills_spacy(text))
    return list(keywords.union(spacy_skills))

def generate_skill_gap_report(jd_skills: List[str], resume_skills: List[str]) -> dict:
    """
    Compares the skills found in the JD with the skills found in the resume.
    Returns a dictionary of matched and missing skills.
    """
    jd_set = set(jd_skills)
    resume_set = set(resume_skills)
    
    return {
        "matched": list(jd_set.intersection(resume_set)),
        "missing": list(jd_set.difference(resume_set)),
        "additional_in_resume": list(resume_set.difference(jd_set))
    }

TRENDING_SKILLS = {
    "langchain": "🔥 Trending",
    "llm": "🔥 Trending",
    "docker": "⚡ In Demand",
    "kubernetes": "⚡ In Demand",
    "fastapi": "⚡ In Demand",
    "pytorch": "🔥 Trending",
    "sql": "⚡ In Demand",
    "react": "⚡ In Demand",
}

def tag_skills(missing_skills: List[str]) -> List[str]:
    tagged = []
    for skill in missing_skills:
        badge = TRENDING_SKILLS.get(skill.lower(), "")
        tagged.append(f"{skill} {badge}".strip())
    return tagged
