from pydantic import BaseModel, EmailStr, conint, Field
from datetime import datetime, date
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

class RoleBaseDto(BaseModel):
    name: str
    code: str

class ResponseRoleDto(RoleBaseDto):
    id: int

class UserRoleBaseDto(BaseModel):
    user_id: int
    role_id: int

class CreateUserRoleDto(UserRoleBaseDto):
    pass

class ResponseUserRoleDto(UserRoleBaseDto):
    id: int
    date_from: datetime
    date_to: Optional[datetime] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None   




