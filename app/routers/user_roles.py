from .. import models, schemas
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/user_roles',
    tags=['User_Roles']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=schemas.ResponseUserRoleDto)
def get_all(db: Session = Depends(get_db)):
    roles = db.query(models.UserRole).all()
    return roles

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUserRoleDto)
def create_userrole(data: schemas.CreateUserRoleDto, db: Session = Depends(get_db)):
    userrole = models.UserRole(**data.dict())
    userrole.user_id = data.user_id
    userrole.role_id = data.role_id
    db.add(userrole)
    db.commit()
    #TODO: dodać unikalność wpisu w bazie o tym samym user_id i role_id
    db.refresh(userrole)
    return userrole