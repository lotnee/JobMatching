
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Set

@dataclass
class JobMatch:
    _job_seeker_id: int
    _job_seeker_name: str
    _job_id: int 
    _job_title: str 
    _job_skills_requirement: Set[str] = field(default_factory=set, hash=True)
    _job_seeker_skills: Set[str] = field(default_factory=set, hash=True)
    _matching_skill_count: int = 0
    _matching_skill_percent: Decimal = 0.0


    @property
    def job_seeker_id(self) -> int:
        return self._job_seeker_id
    
    @property
    def job_seeker_name(self) -> str:
        return self._job_seeker_name
    
    @property
    def job_id(self) -> int:
        return self._job_id
    
    @property 
    def job_title(self) -> str:
        return self.job_title
    
    @property
    def job_skills_requirement(self) -> Set[str]:
        return self._job_skills_requirement
    
    @property
    def job_seeker_skills(self) -> Set[str]:
        return self._job_seeker_skills
    
    @property
    def matching_skill_count(self) -> int:
        return self._matching_skill_count
    
    @property
    def matching_skill_percent(self) -> Decimal:
        return self._matching_skill_percent
    
    @job_seeker_id.setter
    def job_seeker_id(self, new_job_seeker_id):
        if new_job_seeker_id >= 1:
            self._job_seeker_id = new_job_seeker_id
    
    @job_seeker_name.setter
    def job_seeker_name(self, new_job_seeker_name):
        if new_job_seeker_name:
            self._job_seeker_name = new_job_seeker_name
    
    @job_id.setter
    def job_id(self, new_job_id):
        if new_job_id >= 1:
            self._job_id = new_job_id

    @job_title.setter
    def job_title(self, new_job_title):
        if new_job_title:
            self._job_title = new_job_title

    @job_skills_requirement.setter
    def job_skills_requirement(self, new_job_skills_requirement):
        self._job_skills_requirement = new_job_skills_requirement

    @job_seeker_skills.setter
    def job_seeker_skills(self, new_job_seeker_skills):
        self._job_seeker_skills = new_job_seeker_skills
    
    def __post_init__(self):
        self.calculate_matching_skill_count()
        self.calculate_matching_skill_percent()
    
    def calculate_matching_skill_count(self):
        self._matching_skill_count = len(set(self.job_seeker_skills).intersection(self.job_skills_requirement))
    
    def calculate_matching_skill_percent(self):
        if len(self._job_skills_requirement) == 0:
            self._matching_skill_percent = 100.00
        else:
            self._matching_skill_percent = float(self._matching_skill_count) / float(len(self._job_skills_requirement)) * 100
    
    def to_output_dict(self):
        return {
            "jobseeker_id": self._job_seeker_id,
            "jobseeker_name": self._job_seeker_name,
            "job_id": self._job_id,
            "job_title": self._job_title,
            "matching_skill_count": self._matching_skill_count,
            "matching_skill_percent": self._matching_skill_percent

        }


