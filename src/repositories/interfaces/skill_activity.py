



from abc import ABC, abstractmethod
from typing import Union, Sequence
from uuid import UUID

from src.models.skill_activity import SkillActivity
from src.schemas.skill import SkillActivityCreateRequest


class ISkillActivityRepository(ABC):
	
	@abstractmethod
	def create(
		self,
		skill_id: UUID,
		payload: SkillActivityCreateRequest
	) -> Union[SkillActivity, None]:
		raise NotImplementedError

	@abstractmethod
	def find_by_id(
		self,
		id: UUID
	) -> Union[SkillActivity, None]:
		raise NotImplementedError
		
	@abstractmethod
	def find_all_by_skill_id(
		self,
		skill_id: UUID
	) -> Sequence[SkillActivity]:
		raise NotImplementedError
		
	@abstractmethod
	def delete_by_id(
		self,
		id: UUID
	) -> Union[SkillActivity, None]:
		raise NotImplementedError




