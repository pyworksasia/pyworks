from fastapi import Header, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional

from App.Services import AuthService

router = APIRouter()

@router.post("/login", response_model=AuthService.Token)
async def login(form_data: AuthService.LoginRequest):
    response = AuthService.login(form_data)
    return response


@router.get("/profile", response_model=AuthService.User)
async def profile(token: str = Depends(AuthService.oauth2_scheme)):
    current_user = AuthService.get_current_user(token)
    return current_user


@router.get("/logout")
async def logout():
    response = {"message": "Logout successfully"}
    return response

