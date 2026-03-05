from datetime import datetime, timezone
from uuid import UUID
from typing import Union, Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.auth import SignupRequest
from src.repositories.interfaces.user import IUserRepository
from src.schemas.user import UserPatchRequest


class UserRepository(IUserRepository):
	def __init__(
		self,
		db: Session
	):
		self.db = db
	
	def create(
		self,
		payload: SignupRequest
	) -> Union[User, None]:
		user_data = User(
			email=payload.email,
			password_hash=payload.password
		)
		self.db.add(user_data)
		self.db.commit()
		self.db.refresh(user_data)
		return user_data
	
	def find_all(
		self
	) -> Sequence[User]:
		stmt = select(User)
		user_data = self.db.scalars(stmt).all()
		return user_data
		
	def find_by_id(
		self,
		id: UUID
	) -> Union[User, None]:
		stmt = select(User).where(User.id == id)
		user_data = self.db.scalar(stmt)
		return user_data

	def find_by_email(
		self,
		email: str
	) -> Union[User, None]:
		stmt = select(User).where(User.email == email)
		user_data = self.db.scalar(stmt)
		return user_data
	
	def update_by_id(
		self,
		user_id: UUID,
		payload: UserPatchRequest
	) -> Union[User, None]:
		user_data = self.find_by_id(user_id)
		if user_data is None:
			return None
		
		updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
		for key, value in updated_payload.items():
			setattr(user_data, key, value)
		
		self.db.commit()
		self.db.refresh(user_data)
		return user_data
	
	def delete_by_id(
		self,
		user_id: UUID
	) -> Union[User, None]:
		user_data = self.find_by_id(user_id)
		if user_data is None:
			return None
		
		setattr(user_data, "deleted_at", datetime.now(timezone.utc))
		
		self.db.commit()
		self.db.refresh(user_data)
		return user_data

