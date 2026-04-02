from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Pre-load the model to avoid reloading on every function call
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_match_score(jd_text: str, resume_text: str) -> float:
    """
    Computes the cosine similarity between the Job Description and Resume text
    using sentence-transformers. Returns a percentage score (0.0 to 100.0).
    """
    if not jd_text.strip() or not resume_text.strip():
        return 0.0
    
    embeddings = model.encode([jd_text, resume_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # Convert score to percentage and handle potential negative values from cosine
    percentage = max(0.0, float(score)) * 100
    return round(percentage, 1)

def calculate_ats_score(jd_text: str, resume_text: str, missing_skills: list) -> float:
    score = 100

    # Penalize for missing skills
    score -= len(missing_skills) * 5

    # Check keyword density
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())
    if not jd_words:
        return score
        
    overlap = len(jd_words & resume_words) / max(len(jd_words), 1)
    if overlap < 0.3:
        score -= 15

    return float(max(0, min(score, 100)))

def generate_suggestions(missing_skills: list, resume_text: str) -> list:
    suggestions = []
    sections = ["experience", "projects", "skills", "summary"]

    for skill in missing_skills[:5]:  # top 5 missing
        found_in = [s for s in sections if s in resume_text.lower()]
        if found_in:
            suggestions.append(
                f"Consider adding '{skill}' to your {found_in[0]} section if you have relevant experience."
            )
        else:
            suggestions.append(
                f"'{skill}' is required in the JD but not found in your resume. Add it to your Skills section."
            )
    return suggestions
