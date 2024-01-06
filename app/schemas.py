from pydantic import BaseModel, EmailStr, conint, Field
from datetime import datetime
from typing import Optional

class UserBaseDto(BaseModel):
    login: str
    email: EmailStr

class CreateUserDto(UserBaseDto):
    password: str    

class ResponseUserDto(UserBaseDto):
    id: int = Field(alias='user_id')
    created_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True
        populate_by_name = True