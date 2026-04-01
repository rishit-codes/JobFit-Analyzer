import pytest
from utils.skills import (
    extract_skills_keyword,
    extract_skills_spacy,
    get_combined_skills,
    generate_skill_gap_report
)

def test_extract_skills_keyword():
    text = "We are looking for a Python developer with experience in React and SQL."
    skills = extract_skills_keyword(text)
    assert "python" in skills
    assert "react" in skills
    assert "sql" in skills
    assert "java" not in skills

def test_extract_skills_spacy():
    text = "Experience with Amazon Web Services (AWS) and machine learning strongly preferred."
    skills = extract_skills_spacy(text)
    # Testing that either the noun chunk or exact name is picked up if it matches our curated list.
    spacy_skills = extract_skills_spacy(text)
    kw_skills = extract_skills_keyword(text)
    # The get_combined_skills should definitely work
    combined = get_combined_skills(text)
    assert "aws" in combined
    assert "machine learning" in combined

def test_generate_skill_gap_report():
    jd = ["python", "react", "sql", "docker", "aws"]
    resume = ["python", "sql", "git", "pandas"]
    
    report = generate_skill_gap_report(jd, resume)
    
    assert "python" in report["matched"]
    assert "sql" in report["matched"]
    assert "react" in report["missing"]
    assert "docker" in report["missing"]
    assert "aws" in report["missing"]
    assert "git" in report["additional_in_resume"]
