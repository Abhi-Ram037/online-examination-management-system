from datetime import datetime, timedelta, timezone

from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

import os


load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


users = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "student": {
        "username": "student",
        "password": "student123",
        "role": "student"
    }
}


def create_token(username: str, role: str):
    expire_time = datetime.now(timezone.utc) + timedelta(hours=2)

    data = {
        "username": username,
        "role": role,
        "exp": expire_time
    }

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = data.get("username")
        role = data.get("role")

        if username is None or role is None:
            raise HTTPException(
                status_code=401,
                detail="invalid token"
            )

        return {
            "username": username,
            "role": role
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="invalid or expired token"
        )


def admin_required(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="admin access required"
        )

    return current_user


def student_required(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "student":
        raise HTTPException(
            status_code=403,
            detail="student access required"
        )

    return current_user