from pydantic import BaseModel, EmailStr, model_validator


class SignupRequest(BaseModel):
	email: EmailStr
	password: str
	confirm_password: str
	
	@model_validator(mode="after")
	def passwords_match(self):
		if self.password != self.confirm_password:
			raise ValueError("password and confirm_password do not match")
		return self
