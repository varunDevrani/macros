from typing import Union
from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import Session

from src.repositories.interfaces.refresh_token import IRefreshTokenRepository
from src.models.refresh_token import RefreshToken


class RefreshTokenRepository(IRefreshTokenRepository):

	def __init__(
		self,
		db: Session
	):
		self.db = db

	def find_by_token(
		self,
		token: str
	) -> Union[RefreshToken, None]:
		return self.db.query(RefreshToken).filter(RefreshToken.token == token).first()
	
	def find_by_used_id(
		self,
		user_id: UUID
	) -> Union[RefreshToken, None]:
		return self.db.query(RefreshToken).filter(RefreshToken.user_id == user_id).first()

	def delete_token(
		self,
		token: RefreshToken
	):
		self.db.delete(token)
		self.db.commit()

	def create(
		self, 
		user_id: UUID, 
		token: str, 
		issued_at: datetime, 
		expires_at: datetime
	) -> RefreshToken:
		
		refresh_token_data = RefreshToken(
			user_id=user_id,
			token=token,
			issued_at=issued_at,
			expires_at=expires_at
		)

		self.db.add(refresh_token_data)
		self.db.commit()
		self.db.refresh(refresh_token_data)

		return refresh_token_data
