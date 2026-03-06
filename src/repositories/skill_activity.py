





from uuid import UUID

from sqlalchemy.orm import Session

from src.models.skill_activity import SkillActivity
from src.repositories.interfaces.skill_activity import ISkillActivityRepository
from src.schemas.skill import SkillActivityCreateRequest


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
	):
		skill_activity_data = SkillActivity(
			skill_id=skill_id,
			**payload.model_dump()
		)
		
		self.db.add(skill_activity_data)
		self.db.commit()
		self.db.refresh(skill_activity_data)
		return skill_activity_data


