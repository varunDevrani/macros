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
	id: Union[str, None] = None
	name: str
	is_priority: bool
	is_habit_to_protect: bool
	is_completed: bool
	minutes_practised: int

class SkillActivityPartialUpdateRequest(BaseModel):
	id: Union[str, None] = None
	name: Union[str, None] = None
	is_priority: Union[bool, None] = None
	is_habit_to_protect: Union[bool, None] = None
	is_completed: Union[bool, None] = None
	minutes_practised: Union[int, None] = None

class SkillActivityBatchCreateRequest(BaseModel):
	activities: List[SkillActivityCreateRequest] = []

class SkillActivityBatchUpdateRequest(BaseModel):
	activities: List[SkillActivityUpdateRequest] = []

class SkillActivityBatchPartialUpdateRequest(BaseModel):
	activities: List[SkillActivityPartialUpdateRequest] = []

class SkillActivityBatchResponse(BaseModel):
	activities: List[SkillActivityResponse] = []

class SkillResponse(BaseModel):
    id: UUID
    name: str
    is_completed: bool
    total_activites: Union[int, None] = None
    activities: Union[List[SkillActivityResponse], None] = None

class SkillCreateRequest(BaseModel):
    name: str
    activities: Union[List[SkillActivityCreateRequest], None] = None

class SkillPartialUpdateRequest(BaseModel):
    name: str
    is_completed: bool
    
class SkillUpdateRequest(BaseModel):
    name: Union[str, None] = None
    is_completed: Union[bool, None] = None


class SkillsResponse(BaseModel):
	total_skills: int
	skills: Union[List[SkillResponse], None] = None

