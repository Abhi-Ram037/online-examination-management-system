from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas.auth import TokenResponse
from auth import users, create_token


router = APIRouter(tags=["authentication"])


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = users.get(form_data.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    if user["password"] != form_data.password:
        raise HTTPException(
            status_code=401,
            detail="invalid username or password"
        )

    token = create_token(
        user["username"],
        user["role"]
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }