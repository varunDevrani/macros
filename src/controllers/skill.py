


from uuid import UUID
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.repositories.skill import SkillRepository
from src.repositories.skill_activity import SkillActivityRepository
from src.repositories.user import UserRepository
from src.schemas.api_response import SuccessResponse
from src.schemas.skill import SkillActivityCreateRequest, SkillActivityResponse, SkillCreateRequest, SkillResponse
import src.services.skill as services

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
		message="skill activity fectched successfully",
		data=skill_activity_data
	)


def get_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	user_id: UUID,
	db: Session
):
	pass


def get_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID,
	db: Session
):
	pass

