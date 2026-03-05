
from uuid import UUID
from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from src.schemas.skill import SkillActivityCreateRequest, SkillActivityResponse, SkillCreateRequest, SkillResponse
from src.dependencies.database import get_db
from src.dependencies.auth import get_current_user
from src.schemas.api_response import SuccessResponse

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("", status_code=201, response_model=SuccessResponse[SkillResponse])
def create_skill(
	request: Request,
	response: Response,
	payload: SkillCreateRequest,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db),
):
	pass


@router.post("/{skill_id}/activities", status_code=201, response_model=SuccessResponse[SkillActivityResponse])
def create_skill_activity(
	request: Request,
	response: Response,
	payload: SkillActivityCreateRequest,
	user_id: UUID = Depends(get_current_user),
	db: Session = Depends(get_db)
):
	pass

