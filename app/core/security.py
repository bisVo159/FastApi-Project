from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import jwt, JWTError

def create_access_token(data: dict, expires_delta:int = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload if payload.get("exp") >= datetime.now(timezone.utc).timestamp() else None
    except JWTError:
        return None