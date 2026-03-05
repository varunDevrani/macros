from uuid import UUID
from pydantic import BaseModel
from datetime import date

class SkillActivityResponse(BaseModel):
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

