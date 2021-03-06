from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/")
async def read_setting():
    setting = {
        "version": "1.0.0",
        "current_language": "en",
        "languages": {
            "vi": {
                "name": "Vietnam",
            },
            "en": {
                "name": "English",
            },
        },
    }
    return setting
