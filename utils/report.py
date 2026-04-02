import tempfile
import os
from fpdf import FPDF

def generate_pdf_report(score: float, matched: list, missing: list, suggestions: list) -> str:
    """
    Generates a PDF report and returns the path to the temporary file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="JobFit Analysis Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Match Score: {score}%", ln=True)
    
    pdf.cell(200, 10, txt=f"Skills You Have:", ln=True)
    matched_str = ", ".join(matched) if matched else "None"
    pdf.multi_cell(0, 10, txt=matched_str)
    
    pdf.cell(200, 10, txt="Missing Skills:", ln=True)
    missing_str = ", ".join(missing) if missing else "None"
    pdf.multi_cell(0, 10, txt=missing_str)
    
    if suggestions:
        pdf.cell(200, 10, txt="Suggestions:", ln=True)
        for s in suggestions:
            pdf.multi_cell(0, 10, txt=f"- {s}")

    temp_file, path = tempfile.mkstemp(suffix=".pdf")
    os.close(temp_file)
    pdf.output(path)
    return path
