from http import HTTPStatus
from sqlalchemy.orm import Session
from src.exceptions import DomainException, FieldViolation
from src.repositories.interfaces.refresh_token import IRefreshTokenRepository
from src.repositories.interfaces.user import IUserRepository
from src.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from src.utils.jwt_handler import create_token, JWTToken
from datetime import datetime, timezone


def signup(
	payload: SignupRequest,
	db: Session,
	user_repo: IUserRepository
):
	
	user_data = user_repo.find_by_email(payload.email)
	if user_data is not None:
		raise DomainException(
			status_code=HTTPStatus.CONFLICT,
			message="user with email already exists",
			field_violations=[
				FieldViolation(
					field="email",
					message="email already used"
				)
			]
		)
	
	user_data = user_repo.create(payload)
	return user_data

def login(
	payload: LoginRequest,
	user_repo: IUserRepository,
	refresh_token_repo: IRefreshTokenRepository
) -> TokenResponse:
	
	user_data = user_repo.find_by_email(payload.email)

	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials"
		)
	
	if payload.password != user_data.password_hash:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials"
		)
	
	refresh_token_data = refresh_token_repo.find_by_used_id(user_data.id)
	if refresh_token_data is not None and refresh_token_data.expires_at > datetime.now(timezone.utc):
		raise DomainException(
			HTTPStatus.CONFLICT,
			"User is already logged in"
		)
	
	access_token_payload, access_token = create_token(user_data.id, JWTToken.ACCESS_TOKEN)
	refresh_token_payload, refresh_token = create_token(user_data.id, JWTToken.REFRESH_TOKEN)

	refresh_token_repo.create(
		user_data.id,
		refresh_token,
		refresh_token_payload.iat,
		refresh_token_payload.exp
	)

	return TokenResponse(
		access_token=access_token,
		refresh_token=refresh_token
	)