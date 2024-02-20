
from dataclasses import dataclass, field
from typing import Set

@dataclass
class Job:
    _id: int
    _title: str
    _required_skills: Set[str] = field(default_factory=set, hash=True)

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def required_skills(self) -> Set[str]:
        return self._required_skills
    
    @id.setter
    def id(self, new_id):
        self._id = new_id 
    
    @title.setter
    def title(self, new_title):
        self._title = new_title
    
    @required_skills.setter
    def required_skills(self, new_required_skills):
        self._required_skills = new_required_skills

    
    


