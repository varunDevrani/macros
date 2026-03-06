





from uuid import UUID
from typing import Sequence, Union
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.skill_activity import SkillActivity
from src.repositories.interfaces.skill_activity import ISkillActivityRepository
from src.schemas.skill import SkillActivityCreateRequest, SkillActivityPartialUpdateRequest, SkillActivityUpdateRequest


class SkillActivityRepository(ISkillActivityRepository):
	
	def __init__(
		self,
		db: Session
	):
		self.db = db
	
	def create(
		self,
		skill_id: UUID,
		payload: SkillActivityCreateRequest
	) -> Union[SkillActivity, None]:
		skill_activity_data = SkillActivity(
			skill_id=skill_id,
			**payload.model_dump()
		)
		
		self.db.add(skill_activity_data)
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data

	def find_by_id(
		self,
		id: UUID
	) -> Union[SkillActivity, None]:
		stmt = select(SkillActivity).where(SkillActivity.id == id)
		skill_activity_data = self.db.scalar(stmt)
		return skill_activity_data
	
	def find_all_by_skill_id(
		self,
		skill_id: UUID
	) -> Sequence[SkillActivity]:
		stmt = select(SkillActivity).where(SkillActivity.skill_id == skill_id)
		skill_activity_data = self.db.scalars(stmt).all()
		return skill_activity_data
	
	def delete_by_id(
		self,
		id: UUID
	) -> Union[SkillActivity, None]:
		skill_activity_data = self.find_by_id(id)
		
		self.db.delete(skill_activity_data)
		self.db.commit()
		return skill_activity_data
	
	def update_by_id(
		self,
		id: UUID,
		payload: SkillActivityUpdateRequest
	) -> Union[SkillActivity, None]:
		skill_activity_data = self.find_by_id(id)
		if skill_activity_data is None:
			return None
		
		updated_payload = payload.model_dump()
		for key, value in updated_payload.items():
			setattr(skill_activity_data, key, value)
		
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data
	
	def partial_update_by_id(
		self,
		id: UUID,
		payload: SkillActivityPartialUpdateRequest
	) -> Union[SkillActivity, None]:		
		skill_activity_data = self.find_by_id(id)
		if skill_activity_data is None:
			return None
		
		updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
		for key, value in updated_payload.items():
			setattr(skill_activity_data, key, value)
		
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data

