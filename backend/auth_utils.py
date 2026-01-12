import os
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlmodel import Session
from dotenv import load_dotenv
from database import get_session

load_dotenv()

# environment variables for auth
SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
ALGORITHM = os.getenv("AUTH_ALGORITHM")

# database dependancies
db_dependency = Annotated[Session, Depends(get_session)]

# password hashing
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# OAuth2 Bearer Configuration
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
token_dependency = Annotated[str, Depends(oauth2_bearer)]