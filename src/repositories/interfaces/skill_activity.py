



from abc import ABC, abstractmethod
from uuid import UUID

from src.schemas.skill import SkillActivityCreateRequest


class ISkillActivityRepository(ABC):
	
	@abstractmethod
	def create(
		self,
		skill_id: UUID,
		payload: SkillActivityCreateRequest
	):
		raise NotImplementedError


