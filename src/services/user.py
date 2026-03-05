


from http import HTTPStatus
from uuid import UUID
from src.repositories.interfaces.user import IUserRepository
from src.schemas.user import UserPatchRequest
from src.exceptions import DomainException, FieldViolation

def get_users(
	user_repo: IUserRepository
):
	users_data = user_repo.find_all()
	return users_data


def get_user_by_id(
	user_id: UUID,
	user_repo: IUserRepository
):
	user_data = user_repo.find_by_id(user_id)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message=f"user with id {user_id} does not exist",
			field_violations=[
				FieldViolation(
					field="user_id",
					message="user_id not found"
				)
			]
		)
	
	return user_data


def update_user_by_id(
	user_id: UUID,
	payload: UserPatchRequest,
	user_repo: IUserRepository
):
	user_data = user_repo.update_by_id(user_id, payload)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message=f"user with id {user_id} does not exist",
			field_violations=[
				FieldViolation(
					field="user_id",
					message="user_id not found"
				)
			]
		)
	
	return user_data


def delete_user_by_id(
	user_id: UUID,
	user_repo: IUserRepository
):
	user_data = user_repo.delete_by_id(user_id)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message=f"user with id {user_id} does not exist",
			field_violations=[
				FieldViolation(
					field="user_id",
					message="user_id not found"
				)
			]
		)
	
	return user_data