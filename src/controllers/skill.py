from uuid import UUID

from fastapi import Request, Response
from sqlalchemy.orm import Session

import src.services.skill as services
from src.repositories.skill import SkillRepository
from src.repositories.skill_activity import SkillActivityRepository
from src.repositories.user import UserRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.skill import (
    SkillActivityBatchCreateRequest,
    SkillActivityBatchPartialUpdateRequest,
    SkillActivityBatchUpdateRequest,
    SkillActivityCreateRequest,
    SkillActivityPartialUpdateRequest,
    SkillActivityResponse,
    SkillActivityUpdateRequest,
    SkillCreateRequest,
    SkillPartialUpdateRequest,
    SkillResponse,
    SkillUpdateRequest,
)


def create_skill(
	request: Request,
	response: Response,
	payload: SkillCreateRequest,
	user_id: UUID,
	db: Session
) -> SuccessResponse[SkillResponse]:
	user_repo = UserRepository(db)
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_data = services.create_skill(
		payload,
		user_id,
		user_repo,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillResponse](
		message="skill created successfully",
		data=skill_data
	)


def create_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityCreateRequest,
	user_id: UUID,
	db: Session
) -> SuccessResponse[SkillActivityResponse]:
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_activity_data = services.create_skill_activity(
		skill_id,
		payload,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillActivityResponse](
		message="skill activity created successfully",
		data=skill_activity_data
	)


def get_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	user_id: UUID,
	db: Session
):
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_data = services.get_skill_by_id(
		skill_id,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillResponse](
		message="skill fetched successfully",
		data=skill_data
	)


def get_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	db: Session
):
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_activity_data = services.get_skill_activity_by_id(
		skill_id,
		activity_id,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillActivityResponse](
		message="skill fetched successfully",
		data=skill_activity_data
	)


def delete_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	db: Session
):
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_activity_data = services.delete_skill_activity_by_id(
		skill_id,
		activity_id,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillActivityResponse](
		message="skill deleted successfully",
		data=skill_activity_data
	)


def update_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	payload: SkillActivityUpdateRequest,
	user_id: UUID,
	db: Session
):
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_activity_data = services.update_skill_activity_by_id(
		skill_id,
		activity_id,
		payload,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillActivityResponse](
		message="skill activity updated successfully",
		data=skill_activity_data
	)


def partial_update_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	payload: SkillActivityPartialUpdateRequest,
	user_id: UUID,
	db: Session
):
	skill_repo = SkillRepository(db)
	skill_activity_repo = SkillActivityRepository(db)

	skill_activity_data = services.partial_update_skill_activity_by_id(
		skill_id,
		activity_id,
		payload,
		user_id,
		skill_repo,
		skill_activity_repo
	)

	return SuccessResponse[SkillActivityResponse](
		message="skill activity patched successfully",
		data=skill_activity_data
	)


def update_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillUpdateRequest,
	user_id: UUID,
	db: Session
):
	user_repo = UserRepository(db)
	skill_repo = SkillRepository(db)

	skill_data = services.update_skill_by_id(
		skill_id,
		payload,
		user_id,
		user_repo,
		skill_repo
	)

	return SuccessResponse[SkillResponse](
		message="skill updated successfully",
		data=skill_data
	)


def partial_update_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillPartialUpdateRequest,
	user_id: UUID,
	db: Session
):
	user_repo = UserRepository(db)
	skill_repo = SkillRepository(db)

	skill_data = services.partial_update_skill_by_id(
		skill_id,
		payload,
		user_id,
		user_repo,
		skill_repo
	)

	return SuccessResponse[SkillResponse](
		message="skill updated successfully",
		data=skill_data
	)


def create_batch_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityBatchCreateRequest,
	user_id: UUID,
	db: Session
):
	pass


def update_batch_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityBatchUpdateRequest,
	user_id: UUID,
	db: Session
):
	pass


def partial_update_batch_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityBatchPartialUpdateRequest,
	user_id: UUID,
	db: Session
):
	pass
