
import pytest
from test.fixtures import setup_job_csv_path, setup_job_seeker_csv_path,setup_job_list,setup_job_seeker_list,setup_job_match_object

def test_find_matching_skill_count_case1(setup_job_match_object):
    """
    Give a Job with skills = {"R", "Python", "React","C","C++","C#"}
    and a Job Seeker with skills = {"Pyton", "React", "Javascript", "Java"}
    the number of matching skills are 1
    """
    job_match = setup_job_match_object
    job_match.calculate_matching_skill_count()
    assert job_match.matching_skill_count == 2

def test_find_matching_skill_count_case2(setup_job_match_object):
    """
    Given a job with no required skills
    and a job seeker with skills {"C", "Java", "Python"}
    the number of matching skills should be 0
    """
    job_match = setup_job_match_object
    job_match.job_skills_requirement = {}
    job_match.job_seeker_skills = {"C", "Java", "Python"}
    job_match.calculate_matching_skill_count()

    assert job_match.matching_skill_count == 0


def test_finding_matching_skill_count_case3(setup_job_match_object):
    """
    Given a job with required skills {"C", "Java", "Python"}
    and a job seeker with no skills 
    the number of matching skills should be 0
    """
    job_match = setup_job_match_object
    job_match.job_skills_requirement = {"C", "Java", "Python"}
    job_match.job_seeker_skills = {}
    job_match.calculate_matching_skill_count()

    assert job_match.matching_skill_count == 0


def test_calculate_matching_skill_percentage_case1(setup_job_match_object):
    """
    Given a job has 4 skill requirements
    and a job seeker has 6 skills with two matching skills
    the matching skill percent should be  1/3 or 33.33333
    """
    job_match = setup_job_match_object
    job_match.calculate_matching_skill_count()
    job_match.calculate_matching_skill_percent()
    
    assert job_match.matching_skill_percent == float(1)/float(3) * 100

def test_calculate_matching_skill_percentage_case2(setup_job_match_object):
    job_match = setup_job_match_object
    job_match.job_skills_requirement = {}
    job_match.job_seeker_skills = {"C", "Java", "Python"}
    job_match.calculate_matching_skill_count()
    job_match.calculate_matching_skill_percent()
    assert job_match.matching_skill_percent == 100.00