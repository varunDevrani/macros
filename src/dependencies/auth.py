from http import HTTPStatus
from uuid import UUID
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.utils.jwt_handler import JWTToken, decode_token
from src.exceptions import DomainException, FieldViolation



security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UUID:
    
	if not credentials:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
			field_violations=[
				FieldViolation(
					field="credentials",
					message="missing bearer token"
				)
			]
		)
    
	token = decode_token(credentials.credentials)
	
	if token is None or token.token_type != JWTToken.ACCESS_TOKEN:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
			field_violations=[
				FieldViolation(
					field="credentials",
					message="invalid bearer token"
				)
			]
		)
	
	return UUID(token.user_id)
