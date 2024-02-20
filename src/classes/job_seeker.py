from dataclasses import dataclass, field
from typing import List,Set
from src.classes.job_match import JobMatch

@dataclass
class JobSeeker:
    _id: int
    _name: str 
    _skills: Set[str]
    _job_recommendations: List[JobMatch] = field(default_factory=list)

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def skills(self) -> Set[str]:
        return self._skills
    
    @property
    def job_reccomendations(self) -> List[JobMatch]:
        return self._job_reccomendations
    
    @id.setter
    def id(self, new_id: int):
        self._id = new_id
    
    @name.setter
    def name(self, new_name: str):
        self._name = new_name 
    

    @skills.setter
    def skills(self, new_skills: Set[str]):
        self._skills = new_skills
    
    @job_reccomendations.setter
    def job_reccomendations(self, new_job_reccomendations: List[JobMatch]):
        self._job_recommendations = new_job_reccomendations