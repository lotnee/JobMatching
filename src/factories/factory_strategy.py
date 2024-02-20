from dataclasses import dataclass
from typing import Union
from src.factories.job_factory import JobFactory
from src.factories.job_seeker_factory import JobSeekerFactory
from src.factories.job_match_factory import JobMatchFactory
from src.exceptions.exceptions import InvalidObjectType

factories_dict = {
    'Job': JobFactory,
    'Job Seeker': JobSeekerFactory,
    'Job Match': JobMatchFactory
}

@dataclass
class FactoryCreationStrategy:
    factory_type: str 

    def create_object(self, **kwargs):
        try:
            strategy: Union[JobFactory, JobSeekerFactory] = factories_dict[self.factory_type]()
        except KeyError:
            raise InvalidObjectType(f"Object type '{self.factory_type}' is invalid.")

        return strategy.create_object(**kwargs)
    
