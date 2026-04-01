from utils.scoring import get_match_score

def test_get_match_score_high_similarity():
    jd = "We are looking for a Python developer with experience in Django, SQL, and REST APIs."
    resume = "I am a backend developer experienced in Python, Django framework, building RESTful APIs, and writing SQL queries."
    score = get_match_score(jd, resume)
    assert score > 60.0  # Should have a reasonably high similarity score

def test_get_match_score_low_similarity():
    jd = "Looking for a seasoned nurse with ICU experience and CPR certification."
    resume = "I am a frontend web developer skilled in React, CSS, and JavaScript."
    score = get_match_score(jd, resume)
    assert score < 40.0  # Should have a low similarity score

def test_get_match_score_empty_strings():
    assert get_match_score("", "some resume") == 0.0
    assert get_match_score("some jd", "") == 0.0
    assert get_match_score("", "") == 0.0
