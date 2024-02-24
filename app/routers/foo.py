from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/foos',
    tags=['Foos']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseFooDto)
def create_foo():
    return {"ok"}