import os
from typing import Annotated, Optional
from datetime import datetime, timezone
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from dotenv import load_dotenv
from database import get_db

load_dotenv()

SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
ALGORITHM = os.getenv("AUTH_ALGORITHM")

# 1. Standardized DB Dependency
db_dependency = Annotated[Session, Depends(get_db)]

# 2. OAuth2 Scheme
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
token_dependency = Annotated[str, Depends(oauth2_bearer)]

# 3. Enhanced User Validation
async def get_current_user(token: token_dependency):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get('sub')
        user_id: Optional[int] = payload.get('id')
        
        if username is None or user_id is None:
            raise credentials_exception
            
        return {'username': username, 'id': user_id}
        
    except JWTError:
        raise credentials_exception

user_dependency = Annotated[dict, Depends(get_current_user)]
