from .. import models, schemas
from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel

router = APIRouter(
    prefix='/user_roles',
    tags=['User_Roles']
)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseUserRoleDto) 
def get_one(id: int, db: Session = Depends(get_db)):
    roles = db.query(models.UserRole).filter(models.UserRole.id == id).first()
    return roles

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseUserRoleDto])
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
    db.refresh(userrole)
    return userrole

@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ResponseUserRoleDto) 
def update_userrole(id: int, data: schemas.UpdateUserRoleDto, db: Session = Depends(get_db)): 
    userrole_query = db.query(models.UserRole).filter(models.UserRole.id == id)
    userrole_entity = userrole_query.first()
    userrole_query.update({models.UserRole.date_to : data.date_to,
                           models.UserRole.updated_at : datetime.now()}, synchronize_session=False)
    if datetime.now() > datetime.combine(data.date_to, datetime.min.time()):
        userrole_query.update({models.UserRole.is_active : False}, synchronize_session=False)    
    else:
        userrole_query.update({models.UserRole.is_active : True}, synchronize_session=False)   
    db.commit()
    db.refresh(userrole_entity)
    return userrole_entity

@router.delete("/{id}")
def remove_userrole(id: int, db: Session = Depends(get_db)):
    userrole_query = db.query(models.UserRole).filter(models.UserRole.id == id)
    userrole_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 