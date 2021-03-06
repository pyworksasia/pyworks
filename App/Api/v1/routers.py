from fastapi import APIRouter
from App.Api.v1.endpoints import auth, setting

api_router = APIRouter()
api_router.include_router(setting.router, prefix="/setting", tags=["setting"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

