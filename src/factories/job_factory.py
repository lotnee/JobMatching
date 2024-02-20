from abc import ABC, abstractmethod
from typing import Dict, List
from factory_interface import FactoryCreator
from src.classes.job import Job


class JobFactory(FactoryCreator):

    def create_object(self, **kwargs):

        try:
            id = int(kwargs["id"])
            title = kwargs["title"]
            required_skills = super().convert_csv_value_to_set(kwargs["required_skills"])

        except KeyError as e:
            print(f'The following attribute can not be found: {e}')
            exit()

        return Job(_id=id, _title=title, _required_skills=required_skills)
    
  