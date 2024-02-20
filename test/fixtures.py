from src.classes.job import Job
from src.classes.job_seeker import JobSeeker
from src.classes.job_match import JobMatch
from src.exceptions.exceptions import InvalidObjectType
import pytest
from pathlib import Path
from utils import utils


@pytest.fixture
def setup_job_csv_path():
    return Path("data/jobs.csv")

@pytest.fixture
def setup_job_seeker_csv_path():
    return Path("data/jobseekers.csv")

@pytest.fixture
def setup_job_list(setup_job_csv_path):
    data = utils.get_csvs(setup_job_csv_path)
    return data

@pytest.fixture
def setup_job_seeker_list(setup_job_seeker_csv_path):
    data = utils.get_csvs(setup_job_seeker_csv_path)
    return data

@pytest.fixture
def setup_job_match_object():
    job_match = JobMatch(_job_seeker_id=1, 
                         _job_seeker_name="Brian X", 
                         _job_id=1, 
                         _job_title="Software Developer",
                         _job_seeker_skills={"Python", "React", "Javascript", "Java"},
                         _job_skills_requirement={"R", "Python", "React","C","C++","C#"}
                         )
    return job_match