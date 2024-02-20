from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, List, Set, Union
import pandas as pd
import csv
import os
from src.classes.job import Job
from src.classes.job_seeker import JobSeeker
from src.classes.job_match import JobMatch
from src.factories.factory_strategy import FactoryCreationStrategy


MAX_WORKERS = 11
PARALLEL_PROCESSING_FILE_SIZE_CONDITION = 100000


        

def get_csvs(file_path: Path) -> List[Dict[str,str]]:
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = list(csv.DictReader(file))
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = executor.map(data.append, reader)
                list(futures)
    except FileNotFoundError:
        raise FileNotFoundError(f"File path {file_path} does not exist")
    return data




def setup_object(type: str, data: List[Dict[str,Union[str,int]]])->Union[Job,JobSeeker]:
    
    object_list = []

    factory = FactoryCreationStrategy(factory_type=type)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(factory.create_object, **row) for row in data]
        for future in futures:
            object_list.append(future.result())
    return object_list

def find_common_skills(job_seeker_skills: Set[str], job_skills: Set[str]) -> int:
    return len(set(job_seeker_skills).intersection(job_skills))


def construct_job_match_attribute_dict(job_seeker: JobSeeker, job: Job) -> Dict[str, Union[str,int]]:
    job_match_attributes = {}

    job_match_attributes["job_seeker_id"] = job_seeker.id
    job_match_attributes["job_seeker_name"] = job_seeker.name
    job_match_attributes["job_seeker_skills"] = job_seeker.skills

    job_match_attributes["job_id"] = job.id
    job_match_attributes["job_title"] = job.title
    job_match_attributes["job_skills_requirement"] = job.required_skills

    return job_match_attributes


def execute_batch(job_seeker_batch, job_list_batch, future_list):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for job_seeker in job_seeker_batch:
            for job in job_list_batch:
                future = executor.submit(construct_job_match_attribute_dict, job_seeker=job_seeker, job=job)
                future_list.append(future)


        

def setup_job_match(job_seeker_list: List[JobSeeker], job_list: List[Job]) -> List[JobMatch]:
    job_match_attribute_future_list = []
    batch_outer= 100
    batch_inner = 100
    for i in range(0, len(job_seeker_list), batch_outer):
        job_seeker_batch = job_seeker_list[i:i+batch_outer]
        for j in range(0, len(job_list), batch_inner):
            job_list_batch = job_list[j:j+batch_inner]
            execute_batch(job_seeker_batch=job_seeker_batch, job_list_batch=job_list_batch, future_list=job_match_attribute_future_list)

    job_match_attribute_list = [future.result() for future in job_match_attribute_future_list]
    job_match_object_list = setup_object(type="Job Match",data=job_match_attribute_list)
    return job_match_object_list


def create_output(job_match_list: List[JobMatch]) -> pd.DataFrame:
    job_recommendations = pd.DataFrame([job_match.to_output_dict() for job_match in job_match_list])
    job_recommendations.sort_values(by=['jobseeker_id','matching_skill_percent','job_id'], ascending = [True, False, True], inplace=True)
    return job_recommendations




        




        

        

    