



from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

from src.models.skill import Skill
from src.schemas.skill import SkillCreateRequest, SkillPartialUpdateRequest, SkillUpdateRequest


class ISkillRepository(ABC):
	
	@abstractmethod
	def create(
		self,
		user_id: UUID,
		payload: SkillCreateRequest
	) -> Union[Skill, None]:
		raise NotImplementedError
	
	@abstractmethod
	def find_by_id(
		self,
		id: UUID
	) -> Union[Skill, None]:
		raise NotImplementedError

	@abstractmethod
	def find_by_name(
		self,
		name: str
	) -> Union[Skill, None]:
		raise NotImplementedError
	
	@abstractmethod
	def update_by_id(
		self,
		id: UUID,
		payload: SkillUpdateRequest,
	) -> Union[Skill, None]:
		raise NotImplementedError
	
	@abstractmethod
	def partial_update_by_id(
		self,
		id: UUID,
		payload: SkillPartialUpdateRequest
	) -> Union[Skill, None]:
		raise NotImplementedError


	