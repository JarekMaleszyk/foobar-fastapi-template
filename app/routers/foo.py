from .. import models, schemas, oauth2
from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/foos',
    tags=['Foos']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseFooDto)
def create_foo(foo: schemas.CreateFooDto, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    new_foo = models.Foo(user_id = current_user.id, **foo.dict())
    db.add(new_foo)
    db.commit()
    db.refresh(new_foo)
    return new_foo

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseFooDto])
def get_many(search: str,
             limit: int = 10,
             skip: int = 0,
             db: Session = Depends(get_db)):
    foos = db.query(models.Foo).filter(models.Foo.name.contains(search)).order_by(desc(models.Foo.id)).offset(skip).take(limit).all()
    if not foos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Zero foos were found.')
    return foos

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseFooDto)
def get_one(id: int, db: Session = Depends(get_db)):
    foo = db.query(models.Foo).filter(models.Foo.id == id).first()
    if not foo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} was not found.')
    return foo

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ResponseFooDto)
def update_foo(id: int, foo: schemas.UpdateFooDto, db: Session = Depends(get_db)):
    foo_query = db.query(models.Foo).filter(models.Foo.id == id)
    foo_entity = foo_query.first()
    if not foo_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} not found.')
    foo_query.update({models.Foo.name : foo.name, 
                      models.Foo.descritpion : foo.descritpion},
                       synchronize_session=False)
    db.commit()
    db.refresh(foo_entity)
    return foo_entity

@router.delete("/{id}")
def remove_foo(id: int, db: Session = Depends(get_db)):
    foo = db.query(models.Foo).filter(models.Foo.id == id)
    if not foo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} not found.')
    foo.delete(synchronize_session=False)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)