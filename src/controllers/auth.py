


from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.repositories.user import UserRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.auth import SignupRequest
from src.schemas.user import UserResponse
import src.services.auth as services


def signup(
	request: Request,
	response: Response,
	payload: SignupRequest,
	db: Session
) -> SuccessResponse[UserResponse]:
	user_repo = UserRepository(db)
	
	user_data = services.signup(
		payload,
		db,
		user_repo
	)
	
	return SuccessResponse(
		message="user successfully created. verify",
		data=UserResponse.model_validate(user_data)
	)

