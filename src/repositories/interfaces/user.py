from abc import ABC, abstractmethod
from typing import Sequence, Union
from uuid import UUID

from src.models.user import User
from src.schemas.auth import SignupRequest
from src.schemas.user import UserPatchRequest


class IUserRepository(ABC):
	
	@abstractmethod
	def create(
		self,
		payload: SignupRequest
	) -> Union[User, None]:
		raise NotImplementedError
	
	@abstractmethod
	def find_all(
		self
	) -> Sequence[User]:
		raise NotImplementedError
		
	@abstractmethod
	def find_by_id(
		self,
		id: UUID
	) -> Union[User, None]:
		raise NotImplementedError
	
	@abstractmethod
	def find_by_email(
		self,
		email: str
	) -> Union[User, None]:
		raise NotImplementedError

	@abstractmethod
	def update_by_id(
		self,
		user_id: UUID,
		payload: UserPatchRequest
	) -> Union[User, None]:
		raise NotImplementedError
	
	@abstractmethod
	def delete_by_id(
		self,
		user_id: UUID
	) -> Union[User, None]:
		raise NotImplementedError

