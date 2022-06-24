from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserResponse(BaseModel):
    active: bool = Field(True, description="If the user is active")
    first_name: str = Field(None, description="First name of the user", max_length=50)
    last_name: str = Field(None, description="Last name of the user", max_length=50)
    email: EmailStr = Field(description="Email of the user")
    created_at: datetime = Field(description="Datetime when object was created")

    class Config:
        schema_extra = {
            "example": {
                "active": True,
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@email.com",
                "created_at": "2022-06-23 16:00:00",
            }
        }


class UserRequest(UserResponse):
    password: str = Field(
        description="Password of the user", max_length=255, min_length=8
    )

    class Config:
        schema_extra = {
            "example": {
                "active": True,
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@email.com",
                "password": "password",
            }
        }
