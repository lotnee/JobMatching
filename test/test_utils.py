from src.classes.job import Job
from src.classes.job_seeker import JobSeeker
from src.classes.job_match import JobMatch
from src.exceptions.exceptions import InvalidObjectType
from utils import utils
import pytest
from pathlib import Path
import pandas as pd
from test.fixtures import setup_job_csv_path, setup_job_seeker_csv_path,setup_job_list,setup_job_seeker_list,setup_job_match_object



def test_get_csvs_case1():
    """
    Tests when the file path is valid and file exists
    """
    valid_jobs_csv, valid_job_seekers_csv = Path("data/jobs.csv"),Path("data/jobseekers.csv")
    jobs_list = utils.get_csvs(valid_jobs_csv)
    job_seeker_list = utils.get_csvs(valid_job_seekers_csv)
    assert(isinstance(jobs_list, list)  and isinstance(job_seeker_list, list))

def test_get_csvs_case2():
    """
    Tests when the job csv file path is invalid but the job_seeker path is valid, a FileNotFound Exception should be raised
    """
    invalid_jobs_csv, valid_job_seeker_csv = Path("data/invalid_path.csv"), Path("data/jobseekers.csv")
    with pytest.raises(FileNotFoundError) as exc_info:
        valid_jobseeker_list = utils.get_csvs(valid_job_seeker_csv)
        invalid_jobs_list = utils.get_csvs(invalid_jobs_csv)
        
    assert exc_info.type == FileNotFoundError

def test_setup_object_case1(setup_job_list):
    """
        Given a list of dictionaries and the string 'Job', return a list of Job object
    """
    job_list = setup_job_list
    job_object_list = utils.setup_object(type="Job", data=job_list)
    is_not_Job_Object = False 
    for job in job_object_list:
        if not isinstance(job, Job):
            is_not_Job_Object = True
            break 
    assert is_not_Job_Object == False

def test_setup_object_case2(setup_job_seeker_list):
    """
    Given a list of dictionaries of job seeker details and the string Job Seeker
    return a list of JobSeekerObjects
    """
    job_seeker_list = setup_job_seeker_list
    job_seeker_objects_list = utils.setup_object(type="Job Seeker", data=job_seeker_list)
    is_not_job_seeker_object = False

    for job_seeker in job_seeker_objects_list:
        if not isinstance(job_seeker, JobSeeker):
            is_not_job_seeker_object = True
            break
    assert is_not_job_seeker_object == False

def test_setup_object_case3(setup_job_seeker_list):
    """
    Given a list of dictionaries of job seeker details and a string 'fail'
    raise a InvalidObjectType 
    """
    with pytest.raises(InvalidObjectType) as exc_info:
            result = utils.setup_object(type="fail", data=setup_job_seeker_list)
    assert exc_info.type == InvalidObjectType
        




def test_setup_job_match_case1(setup_job_seeker_list, setup_job_list):
    """
    Test whether setup_job_match returns the right type (should return List[JobMatch])
    """

    job_list, job_seeker_list = setup_job_list,setup_job_seeker_list
    job_obj_list, job_seeker_obj_list = utils.setup_object(type="Job", data=job_list), utils.setup_object("Job Seeker", data=job_seeker_list)
    job_match_obj_list = utils.setup_job_match(job_seeker_list=job_seeker_obj_list, job_list=job_obj_list)
    is_not_job_match_object = False

    for job_match in job_match_obj_list:
        if not isinstance(job_match, JobMatch):
            is_not_job_match_object = True 
            break 
    assert is_not_job_match_object == False


def test_setup_job_match_case1(setup_job_seeker_list, setup_job_list):
    """
    Test whether setup_job_match returns the right type (should return List[JobMatch])
    """

    job_list, job_seeker_list = setup_job_list,setup_job_seeker_list
    job_obj_list, job_seeker_obj_list = utils.setup_object(type="Job", data=job_list), utils.setup_object("Job Seeker", data=job_seeker_list)
    job_match_obj_list = utils.setup_job_match(job_seeker_list=job_seeker_obj_list, job_list=job_obj_list)
    is_not_job_match_object = False

    for job_match in job_match_obj_list:
        if not isinstance(job_match, JobMatch):
            is_not_job_match_object = True 
            break 
    assert is_not_job_match_object == False

def test_setup_job_match_case2(setup_job_seeker_list, setup_job_list):
    """
    Test whether setup_job_match returns the correct number of results
    """

    job_list, job_seeker_list = setup_job_list,setup_job_seeker_list
    job_obj_list, job_seeker_obj_list = utils.setup_object(type="Job", data=job_list), utils.setup_object("Job Seeker", data=job_seeker_list)
    job_match_obj_list = utils.setup_job_match(job_seeker_list=job_seeker_obj_list, job_list=job_obj_list)

    assert len(job_match_obj_list) == len(job_obj_list) * len(job_seeker_obj_list)







    


    
    



