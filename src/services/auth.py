from http import HTTPStatus
from sqlalchemy.orm import Session
from src.exceptions import DomainException, FieldViolation
from src.repositories.interfaces.user import IUserRepository
from src.schemas.auth import SignupRequest


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

