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
