from typing import Optional
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    active: bool
    first_name: str
    last_name: str
    email: EmailStr


class UserRequest(UserResponse):
    active: Optional[bool] = True
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None