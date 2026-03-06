


from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.repositories.refresh_token import RefreshTokenRepository
from src.repositories.user import UserRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.auth import LoginRequest, SignupRequest, TokenResponse
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

def login(
	request: Request,
	response: Response,
	payload: LoginRequest,
	db: Session
) -> SuccessResponse[TokenResponse]:
	
	user_repo = UserRepository(db)
	refresh_token_repo = RefreshTokenRepository(db)
	
	token_data = services.login(
		payload,
		user_repo,
		refresh_token_repo
	)

	return SuccessResponse[TokenResponse](
		message="User logged in. Verify OTP from mail.",
		data=token_data
	)
