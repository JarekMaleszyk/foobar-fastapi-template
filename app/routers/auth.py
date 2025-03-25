from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

from typing import Annotated

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schemas.TokenDto)
def login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.login == user_credentials.username).first()
    # print(user.login)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid credentials.')
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid credentials.')
    try:
        access_token = oauth2.create_accesss_token(data = {"login": user.login})     
    except Exception as ex:
        print(ex)
    return {"access_token": access_token, "token_type": "bearer"}