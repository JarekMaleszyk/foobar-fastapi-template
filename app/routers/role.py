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

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    roles = db.query(models.Role).all()
    return roles