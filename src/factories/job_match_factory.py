from abc import ABC, abstractmethod
from typing import Dict, List
from factory_interface import FactoryCreator
from src.classes.job_match import JobMatch


class JobMatchFactory(FactoryCreator):

    def create_object(self, **kwargs):

        try:
            job_seeker_id = int(kwargs["job_seeker_id"])
            job_seeker_name = kwargs["job_seeker_name"]
            job_seeker_skills = kwargs["job_seeker_skills"]

            job_id = kwargs["job_id"]
            job_title = kwargs["job_title"]
            job_skills_requirements = kwargs["job_skills_requirement"]

        except KeyError as e:
            print(f'The following attribute can not be found: {e}')
            exit()

        return JobMatch(_job_seeker_id=job_seeker_id, 
                        _job_seeker_name=job_seeker_name, 
                        _job_seeker_skills=job_seeker_skills, 
                        _job_skills_requirement=job_skills_requirements, 
                        _job_id=job_id, 
                        _job_title=job_title)
    

  