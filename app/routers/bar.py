from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/bars',
    tags=['Bars']
)

@router.post("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseBarDto)
def create_bar(id: int, bar: schemas.CreateBarDto, db: Session = Depends(get_db)):
    # print(f'INPUT =>>>>>>>>>>> {bar.is_active}')
    foo = db.query(models.Foo).filter(models.Foo.id == id).first()
    if not foo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Foo with id: {id} was not found.')
    bar_check = db.query(models.Bar).filter(models.Bar.foo_id == id).first()
    if bar_check:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Foo with id: {id} has already its own bar with id: {bar_check.id}.')    
    new_bar = models.Bar(foo_id = id, **bar.dict())
    db.add(new_bar)
    db.commit()
    db.refresh(new_bar)
    return new_bar

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseBarDto)
def get_one(id: int, db: Session = Depends(get_db)):
    bar = db.query(models.Bar).filter(models.Bar.id == id).first()
    if not bar:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Bar with id: {id} was not found.')
    return bar

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ResponseBarDto)
def update_bar(id: int, bar: schemas.UpdateBarDto, db: Session = Depends(get_db)):
    bar_query = db.query(models.Bar).filter(models.Bar.id == id)
    bar_entity = bar_query.first()
    if not bar_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Bar with id: {id} not found.')
    bar_query.update({models.Bar.is_active : bar.is_active},
                       synchronize_session=False)
    db.commit()
    db.refresh(bar_entity)
    return bar_entity

@router.delete("/{id}")
def remove_bar(id: int, db: Session = Depends(get_db)):
    bar = db.query(models.Bar).filter(models.Bar.id == id)
    if not bar:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Bar with id: {id} not found.')
    bar.delete(synchronize_session=False)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)