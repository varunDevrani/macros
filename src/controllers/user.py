


from uuid import UUID
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.repositories.user import UserRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.user import UserPatchRequest, UserResponse, UsersResponse
import src.services.user as services


def get_users(
	request: Request,
	response: Response,
	db: Session
)-> SuccessResponse[UsersResponse]:
	
	user_repo = UserRepository(db)
	
	users_data = services.get_users(
		user_repo
	)
	
	return SuccessResponse(
		message="users fetched successfully",
		data=UsersResponse(
			total_users=len(users_data),
			users=[UserResponse.model_validate(data) for data in users_data]
		)
	)


def get_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	db: Session
) -> SuccessResponse[UserResponse]:
	user_repo = UserRepository(db)
	
	user_data = services.get_user_by_id(
		user_id,
		user_repo
	)
	
	return SuccessResponse(
		message=f"user with id {user_id} fetched successfully",
		data=UserResponse.model_validate(user_data)
	)


def update_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	payload: UserPatchRequest,
	db: Session
) -> SuccessResponse[UserResponse]:
	user_repo = UserRepository(db)
	
	user_data = services.update_user_by_id(
		user_id,
		payload,
		user_repo
	)
	
	return SuccessResponse(
		message=f"user with id {user_id} updated successfully",
		data=UserResponse.model_validate(user_data)
	)


def delete_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	db: Session
) -> SuccessResponse[UserResponse]:
	user_repo = UserRepository(db)
	
	user_data = services.delete_user_by_id(
		user_id,
		user_repo
	)
	
	return SuccessResponse(
		message=f"user with id {user_id} deleted successfully",
		data=UserResponse.model_validate(user_data)
	)