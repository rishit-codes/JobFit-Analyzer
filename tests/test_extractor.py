import pytest
import os
from reportlab.pdfgen import canvas
from utils.extractor import extract_resume_text

@pytest.fixture
def sample_pdf(tmp_path):
    """Generates a simple PDF file with dummy text for testing."""
    pdf_path = tmp_path / "sample_resume.pdf"
    
    # Create a basic PDF with reportlab
    c = canvas.Canvas(str(pdf_path))
    c.drawString(100, 750, "John Doe")
    c.drawString(100, 730, "Software Engineer")
    c.drawString(100, 710, "Skills: Python, SQL, Streamlit")
    c.save()
    
    return str(pdf_path)

def test_extract_resume_text(sample_pdf):
    extracted_text = extract_resume_text(sample_pdf)
    
    assert "John Doe" in extracted_text
    assert "Software Engineer" in extracted_text
    assert "Python, SQL, Streamlit" in extracted_text

def test_extract_resume_text_invalid_file():
    with pytest.raises(ValueError):
        extract_resume_text("non_existent_file.pdf")
