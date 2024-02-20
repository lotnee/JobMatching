import pytest
from test.fixtures import setup_job_seeker_list, setup_job_list, setup_job_seeker_csv_path, setup_job_csv_path
from utils import utils

def test_create_result_output(setup_job_seeker_list,setup_job_list):
    job_obj_list, job_seeker_obj_list = utils.setup_object("Job", setup_job_list), utils.setup_object("Job Seeker", setup_job_seeker_list)
    job_match_list = utils.setup_job_match(job_seeker_list=job_seeker_obj_list, job_list=job_obj_list)
    output = utils.create_output(job_match_list=job_match_list)

    assert output.shape[0] == len(job_obj_list) * len(job_seeker_obj_list)
