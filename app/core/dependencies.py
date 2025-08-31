from fastapi import HTTPException, Header
from app.core.config import settings
from app.core.security import verify_access_token


def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

def get_current_user(token: str = Header(...)):
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return payload
