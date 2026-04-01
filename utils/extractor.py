import pdfplumber

def extract_resume_text(pdf_file) -> str:
    """
    Extracts text from a given PDF file using pdfplumber.
    Returns the extracted text as a single whitespace-separated string.
    """
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text_pages = [page.extract_text() or "" for page in pdf.pages]
            return " ".join(text_pages).strip()
    except Exception as e:
        raise ValueError(f"Failed to extract text from PDF: {e}")



