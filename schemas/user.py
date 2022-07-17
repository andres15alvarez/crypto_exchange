from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    active: bool = Field(True, description="If the user is active")
    first_name: str = Field(None, description="First name of the user", max_length=50)
    last_name: str = Field(None, description="Last name of the user", max_length=50)
    email: EmailStr = Field(description="Email of the user")

    class Config:
        schema_extra = {
            "example": {
                "active": True,
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@email.com",
            }
        }

class UserResponse(UserBase):
    created_at: datetime = Field(description="Datetime when object was created")

    class Config:
        schema_extra = {
            "example": {
                "active": True,
                "created_at": "2022-07-17T15:40:00",
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@email.com",
                "password": "password",
            }
        }


class UserRequest(UserBase):
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
