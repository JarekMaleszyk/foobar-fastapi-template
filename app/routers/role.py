from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/roles',
    tags=['Roles']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseRoleDto]) 
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Role).all()

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseRoleDto)
def get_role(db: Session = Depends(get_db)):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Role with id: {id} was not found.')
    return role