



from typing import Union
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm.session import Session

from src.models.skill import Skill
from src.repositories.interfaces.skill import ISkillRepository
from src.schemas.skill import SkillCreateRequest, SkillPartialUpdateRequest, SkillUpdateRequest


class SkillRepository(ISkillRepository):
	
	def __init__(
		self,
		db: Session
	):
		self.db = db
	
	def create(
		self,
		user_id: UUID,
		payload: SkillCreateRequest
	) -> Union[Skill, None]:
		skill_data = Skill(
			user_id=user_id,
			name=payload.name
		)
		
		self.db.add(skill_data)
		self.db.commit()
		self.db.refresh(skill_data)
		return skill_data
		
	
	def find_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		stmt = select(Skill).where(Skill.id == id)
		skill_data = self.db.scalar(stmt)
		return skill_data
	
	def find_by_name(
		self,
		name: str
	) -> Union[Skill, None]:
		stmt = select(Skill).where(Skill.name == name)
		skill_data = self.db.scalar(stmt)
		return skill_data

	def update_by_id(
		self,
		id: UUID,
		payload: SkillUpdateRequest,
	) -> Union[Skill, None]:
		skill_data = self.find_by_id(id)
		if skill_data is None:
			return None
		
		updated_payload = payload.model_dump()
		for key, value in updated_payload.items():
			setattr(skill_data, key, value)
		
		self.db.commit()
		self.db.refresh(skill_data)
		return skill_data
	
	def partial_update_by_id(
		self,
		id: UUID,
		payload: SkillPartialUpdateRequest
	) -> Union[Skill, None]:
		skill_data = self.find_by_id(id)
		if skill_data is None:
			return None
		
		updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
		for key, value in updated_payload.items():
			setattr(skill_data, key, value)
		
		self.db.commit()
		self.db.refresh(skill_data)
		return skill_data

