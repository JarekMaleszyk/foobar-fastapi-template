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
def create_foo(foo: schemas.CreateFooDto, db: Session = Depends(get_db)):
    new_foo = models.Foo(**foo.dict())
    new_foo.user_id = 1
    db.add(new_foo)
    db.commit()
    db.refresh(new_foo)
    return new_foo

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseFooDto])
def get_many(limit: int = 10,
             skip: int = 0,
             db: Session = Depends(get_db)):
    foo = db.query(models.Foo).filter(models.Foo.id == id).first()
    if not foo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} was not found.')
    return foo

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseFooDto)
def get_one(id: int, db: Session = Depends(get_db)):
    foo = db.query(models.Foo).filter(models.Foo.id == id).first()
    if not foo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} was not found.')
    return foo

