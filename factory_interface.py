from abc import ABC, abstractmethod
from typing import Set

class FactoryCreator(ABC):

    @abstractmethod
    def create_object(self):
        raise NotImplementedError("create_object method must be implemented") 
    
    def convert_csv_value_to_set(self, csv_string: str) -> Set[str]:
        csv_value_list = [skill.strip() for skill in csv_string.split(',')]
        csv_set = set(csv_value_list)
        return csv_set
         

