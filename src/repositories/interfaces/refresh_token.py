from typing import Union
from datetime import datetime
from uuid import UUID
from abc import ABC, abstractmethod

from src.models.refresh_token import RefreshToken


class IRefreshTokenRepository(ABC):

	@abstractmethod
	def find_by_token(
		self,
		token: str
	) -> Union[RefreshToken, None]:
		raise NotImplementedError
	
	@abstractmethod
	def find_by_used_id(
		self,
		user_id: UUID
	) -> Union[RefreshToken, None]:
		raise NotImplementedError
	
	@abstractmethod
	def delete_token(
		self,
		token: RefreshToken
	):
		raise NotImplementedError

	@abstractmethod
	def create(
		self, 
		user_id: UUID, 
		token: str, 
		issued_at: datetime, 
		expires_at: datetime
	) -> RefreshToken:
		raise NotImplementedError
