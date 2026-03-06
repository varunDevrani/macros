from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from src.dependencies.database import get_db
from src.schemas.auth import LoginRequest, SignupRequest
from src.schemas.api_response import SuccessResponse
import src.controllers.auth as controllers
from src.schemas.user import UserResponse


router = APIRouter(
	prefix="/auth",
	tags=["auth"]
)


@router.post("/signup", status_code=201, response_model=SuccessResponse[UserResponse])
def signup(
	request: Request,
	response: Response,
	payload: SignupRequest,
	db: Session = Depends(get_db)
):
	return controllers.signup(
		request,
		response,
		payload,
		db
	)

@router.post("/login")
def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    return controllers.login(
        request,
        response,
        payload,
        db
	)
