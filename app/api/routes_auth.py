from fastapi import APIRouter
from app.schemas.authInput import AuthInput
from app.core.security import create_access_token

router= APIRouter()

@router.post("/login")
def login(auth_input: AuthInput):
    if auth_input.username != "admin" or auth_input.password != "password":
        return {"error": "Invalid credentials"}
    access_token = create_access_token(data={"sub": auth_input.username})
    return {"access_token": access_token, "token_type": "bearer"}