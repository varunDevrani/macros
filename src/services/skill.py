



from http import HTTPStatus
from typing import List
from uuid import UUID
from src.exceptions import DomainException, FieldViolation
from src.repositories.interfaces.skill import ISkillRepository
from src.repositories.interfaces.skill_activity import ISkillActivityRepository
from src.repositories.interfaces.user import IUserRepository
from src.schemas.skill import SkillActivityCreateRequest, SkillActivityPartialUpdateRequest, SkillActivityResponse, SkillActivityUpdateRequest, SkillCreateRequest, SkillPartialUpdateRequest, SkillResponse, SkillUpdateRequest


def create_skill(
	payload: SkillCreateRequest,
	user_id: UUID,
	user_repo: IUserRepository,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	
	user_data = user_repo.find_by_id(user_id)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="user does not exist",
			field_violations=[
				FieldViolation(
					field="user_id"
				)
			]
		)
	
	skill_data = skill_repo.find_by_name(payload.name)
	if skill_data is not None:
		raise DomainException(
			status_code=HTTPStatus.CONFLICT,
			message="skill already exist",
			field_violations=[
				FieldViolation(
					field="name",
					message="duplicate name"
				)
			]
		)
	
	skill_data = skill_repo.create(
		user_id,
		payload
	)
	
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
			message="skill creation failed"
		)
	
	activities: List[SkillActivityResponse] = []
	if payload.activities is not None:
		
		for activity in payload.activities:
			skill_activity_data = skill_activity_repo.create(
				skill_data.id,
				activity
			)
			activities.append(SkillActivityResponse.model_validate(skill_activity_data))
	
	return SkillResponse(
		id=skill_data.id,
		name=skill_data.name,
		is_completed=skill_data.is_completed,
		total_activites=len(activities),
		activities=activities
	)


def create_skill_activity(
	skill_id: UUID,
	payload: SkillActivityCreateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	skill_activity_data = skill_activity_repo.create(
		skill_id,
		payload
	)
	
	return SkillActivityResponse.model_validate(skill_activity_data)


def get_skill_by_id(
	skill_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	activities: List[SkillActivityResponse] = []
	skill_activity_data = skill_activity_repo.find_all_by_skill_id(skill_data.id)
	for activity in skill_activity_data:
		activities.append(SkillActivityResponse.model_validate(activity))
	
	return SkillResponse(
		id=skill_data.id,
		name=skill_data.name,
		is_completed=skill_data.is_completed,
		total_activites=len(activities),
		activities=activities
	)


def get_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	skill_activity_data = skill_activity_repo.find_by_id(activity_id)
	if skill_activity_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill activity does not exist"
		)
	
	return SkillActivityResponse.model_validate(skill_activity_data)


def delete_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
		
	
	skill_activity_data = skill_activity_repo.find_by_id(activity_id)
	if skill_activity_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill activity does not exist"
		)
	
	skill_activity_data = skill_activity_repo.delete_by_id(activity_id)
	
	return SkillActivityResponse.model_validate(skill_activity_data)


def update_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	payload: SkillActivityUpdateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
		
	
	skill_activity_data = skill_activity_repo.find_by_id(activity_id)
	if skill_activity_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill activity does not exist"
		)
	
	skill_activity_data = skill_activity_repo.update_by_id(activity_id, payload)
	
	return SkillActivityResponse.model_validate(skill_activity_data)


def partial_update_skill_activity_by_id(
	skill_id: UUID,
	activity_id: UUID,
	payload: SkillActivityPartialUpdateRequest,
	user_id: UUID,
	skill_repo: ISkillRepository,
	skill_activity_repo: ISkillActivityRepository
):
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
		
	
	skill_activity_data = skill_activity_repo.find_by_id(activity_id)
	if skill_activity_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill activity does not exist"
		)
	
	skill_activity_data = skill_activity_repo.partial_update_by_id(activity_id, payload)
	
	return SkillActivityResponse.model_validate(skill_activity_data)


def update_skill_by_id(
	skill_id: UUID,
	payload: SkillUpdateRequest,
	user_id: UUID,
	user_repo: IUserRepository,
	skill_repo: ISkillRepository
):
	user_data = user_repo.find_by_id(user_id)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="user does not exist"
		)
	
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	skill_data = skill_repo.update_by_id(skill_id, payload)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	return SkillResponse(
		id=skill_data.id,
		name=skill_data.name,
		is_completed=skill_data.is_completed
	)


def partial_update_skill_by_id(
	skill_id: UUID,
	payload: SkillPartialUpdateRequest,
	user_id: UUID,
	user_repo: IUserRepository,
	skill_repo: ISkillRepository
):
	user_data = user_repo.find_by_id(user_id)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="user does not exist"
		)
	
	skill_data = skill_repo.find_by_id(skill_id)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	skill_data = skill_repo.partial_update_by_id(skill_id, payload)
	if skill_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="skill does not exist"
		)
	
	return SkillResponse(
		id=skill_data.id,
		name=skill_data.name,
		is_completed=skill_data.is_completed
	)


