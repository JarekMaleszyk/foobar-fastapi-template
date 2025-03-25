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

@router.post("/init", status_code=status.HTTP_201_CREATED, response_model=List[schemas.ResponseRoleDto]) 
def init_roles(db: Session = Depends(get_db)):
    
    if db.query(models.Role).first():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Roles can be initialized only once.')
                            
    init_roles: list(dict(str, str)) = [
            {"name": "Administrator", "code": "ADMIN"},
            {"name": "Operator", "code": "OPER"},
            {"name": "User", "code": "USER"},
            {"name": "Viewer", "code": "VIEW"},
        ]

    for init_role in init_roles:
        new_role = models.Role(name = init_role["name"], code = init_role["code"])
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        print(f"New role added: {new_role.code}")

    return db.query(models.Role).all()
