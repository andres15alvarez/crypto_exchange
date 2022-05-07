from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr = Field(description='Email of the user')
    password: str = Field(description='Password of the user', max_length=255, min_length=8)

    class Config:
        schema_extra = {
            'example': {
                'email': 'johndoe@email.com',
                'password': 'password'
            }
        }


class LoginResponse(BaseModel):
    token: str

    class Config:
        schema_extra = {
            'example': {
                'token': ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                '.eyJzdWIiOiJhbmRyZXMxNWFsdmFyZXpAZ21haWwuY29tIiwiZXhwIjoxNjUyMDI1NDIwfQ'
                '.rNyO6fAq1Bzj2DkhYGQhLbI00S1QUuXWz294orNnwb0'
                )
            }
        }
