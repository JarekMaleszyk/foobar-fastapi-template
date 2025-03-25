from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUserDto)
def create_user(user: schemas.CreateUserDto, db: Session = Depends(get_db)):
    """
    Create a new user in the database.

    Args:
        user (schemas.CreateUserDto): The user data to create.
        db (Session): The database session.

    Returns:
        schemas.ResponseUserDto: The created user data.

    Raises:
        HTTPException: If a user with the same login or email already exists.
    """
    user_check = db.query(models.User).filter(models.User.login == user.login or models.User.email == user.email).first()
    if user_check:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'User with the same login or email already exists in the database.')
    hashed_password = utils.hash(user.password)    #hash password
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponseUserDto])
def search_user(db: Session = Depends(get_db),
                email: Optional[str] = '',
                limit: int = 10,
                skip: int = 0):
    """
    Search for users in the database by email.

    Args:
        db (Session): The database session.
        email (Optional[str]): The email to search for.
        limit (int): The maximum number of users to return.
        skip (int): The number of users to skip.

    Returns:
        List[schemas.ResponseUserDto]: The list of found users.

    Raises:
        HTTPException: If no users are found.
    """
    users = db.query(models.User).filter(models.User.email.contains(email)).order_by(desc(models.User.created_at)).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user was found.')
    return users

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseUserDto)
def get_user(id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.

    Args:
        id (int): The user ID.
        db (Session): The database session.

    Returns:
        schemas.ResponseUserDto: The user data.

    Raises:
        HTTPException: If the user with the given ID is not found.
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id:{id} was not found.')
    return user