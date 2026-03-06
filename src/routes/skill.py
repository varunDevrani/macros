
from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from src.schemas.skill import SkillActivityCreateRequest, SkillActivityResponse, SkillCreateRequest, SkillResponse
from src.dependencies.database import get_db
from src.dependencies.auth import get_current_user
from src.schemas.api_response import SuccessResponse
import src.controllers.skill as controllers


router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", status_code=201, response_model=SuccessResponse[SkillResponse])
def create_skill(
	request: Request,
	response: Response,
	payload: SkillCreateRequest,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db),
):
	return controllers.create_skill(
		request,
		response,
		payload,
		user_id,
		db
	)


@router.post("/{skill_id}/activities", status_code=201, response_model=SuccessResponse[SkillActivityResponse])
def create_skill_activity(
	request: Request,
	response: Response,
	skill_id: UUID,
	payload: SkillActivityCreateRequest,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	return controllers.create_skill_activity(
		request,
		response,
		skill_id,
		payload,
		user_id,
		db
	)


@router.get("/{skill_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillResponse])
@router.get("/{skill_id}/activities", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillResponse])
def get_skill_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	return controllers.get_skill_by_id(
		request,
		response,
		skill_id,
		user_id,
		db
	)


@router.get("/{skill_id}/activities/{activity_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillActivityResponse])
def get_skill_activity_by_id(
	request: Request,
	response: Response,
	skill_id: UUID,
	activity_id: UUID,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	return controllers.get_skill_activity_by_id(
		request,
		response,
		skill_id,
		activity_id,
		user_id,
		db
	)
