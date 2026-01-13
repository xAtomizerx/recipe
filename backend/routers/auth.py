from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from jose import jwt
from pydantic import BaseModel
from models import User
from auth_utils import bcrypt_context, db_dependency, SECRET_KEY, ALGORITHM


router = APIRouter(prefix='/auth', tags=['auth'])


class UserCreateRequest(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

#User Helpers
def authenticate_user(username: str, password: str, db):
    statement = select(User).where(User.username == username)
    user = db.exec(statement).first()
    
    # verify password
    if not user or not user.verify_password(password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# Routes for signup to add user to database

@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: UserCreateRequest):
    # Checking to see if user exists
    statement = select(User).where(User.username == create_user_request.username)
    existing_user = db.exec(statement).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username already registered"
        )

    # Hashing Password and Creating User Instance
    new_user = User(
        username=create_user_request.username,
        email=create_user_request.email,
        hashed_password=User.get_password_hash(create_user_request.password)
    )

    # Save user to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh to get the generated ID from the DB

    return {"message": "User created successfully", "user_id": new_user.id}

# create jwt token
@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}