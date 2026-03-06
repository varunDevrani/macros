from uuid import UUID
from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Union, List

class SkillActivityResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)
	
	id: UUID
	entry_date: date
	name: str
	is_priority: bool
	is_habit_to_protect: bool
	is_completed: bool
	minutes_practised: int


class SkillActivityCreateRequest(BaseModel):
	name: str
	is_priority: bool = False
	is_habit_to_protect: bool = False
	is_completed: bool = False
	minutes_practised: int = 0


class SkillActivityUpdateRequest(BaseModel):
	name: str
	is_priority: bool
	is_habit_to_protect: bool
	is_completed: bool
	minutes_practised: int

class SkillResponse(BaseModel):
    id: UUID
    name: str
    is_completed: bool
    total_activites: int
    activities: Union[List[SkillActivityResponse], None] = None

class SkillCreateRequest(BaseModel):
    name: str
    activities: Union[List[SkillActivityCreateRequest], None] = None
    
class SkillUpdateRequest(BaseModel):
    name: Union[str, None] = None
    is_completed: Union[bool, None] = None
    activities: Union[List[SkillActivityUpdateRequest], None] = None

class SkillsResponse(BaseModel):
	total_skills: int
	skills: Union[List[SkillResponse], None] = None

