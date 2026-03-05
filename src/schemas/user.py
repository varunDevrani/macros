from typing import List, Union
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)
	
	id: UUID
	first_name: Union[str, None] = None
	last_name: Union[str, None] = None
	email: str
	profile_pic_url: Union[str, None] = None


class UsersResponse(BaseModel):
	total_users: int
	users: List[UserResponse] = []
	

# TODO: add min and max limits in names
class UserPatchRequest(BaseModel):
	first_name: Union[str, None] = None
	last_name: Union[str, None] = None


