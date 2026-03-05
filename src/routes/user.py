from http import HTTPStatus
from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session
from uuid import UUID

from src.dependencies.database import get_db
from src.schemas.api_response import SuccessResponse
from src.schemas.user import UserPatchRequest, UsersResponse, UserResponse
import src.controllers.user as controllers


router = APIRouter(
	prefix="/users",
	tags=["users"]
)


@router.get("", status_code=HTTPStatus.OK, response_model=SuccessResponse[UsersResponse])
def get_users(
	request: Request,
	response: Response,
	db: Session = Depends(get_db)
):
	return controllers.get_users(
		request,
		response,
		db
	)


@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[UserResponse])
def get_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	db: Session = Depends(get_db)
):
	return controllers.get_user_by_id(
		request,
		response,
		user_id,
		db
	)


@router.patch("/{user_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[UserResponse])
def update_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	payload: UserPatchRequest,
	db: Session = Depends(get_db)
):
	return controllers.update_user_by_id(
		request,
		response,
		user_id,
		payload,
		db
	)


@router.delete("/{user_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[UserResponse])
def delete_user_by_id(
	request: Request,
	response: Response,
	user_id: UUID,
	db: Session = Depends(get_db)
):
	return controllers.delete_user_by_id(
		request,
		response,
		user_id,
		db
	)
