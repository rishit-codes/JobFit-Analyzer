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

import requests
from bs4 import BeautifulSoup

def scrape_jd_from_url(url: str) -> str:
    """
    Scrapes the job description from a given URL.
    Returns the parsed text.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try common selectors
        for selector in ["div.job-description", "div.description", "section.content", "article"]:
            el = soup.select_one(selector)
            if el:
                return el.get_text(separator=" ", strip=True)

        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return ""
