from abc import ABC, abstractmethod
from typing import List
from factory_interface import FactoryCreator
from src.classes.job_seeker import JobSeeker

class JobSeekerFactory(FactoryCreator):

    def create_object(self, **kwargs):
        try:
            id = int(kwargs["id"])
            name = kwargs["name"]
            skills = super().convert_csv_value_to_set(kwargs["skills"])

        except KeyError as e:
            print(f'The following attribute can not be found: {e}')
            exit()

        return JobSeeker(_id=id, _name=name, _skills=skills)        
    
