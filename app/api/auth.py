from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.domain import schemas

router = APIRouter(tags=["Auth"])

@router.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Demo credentials
    if form_data.username != "user1" or form_data.password != "password123":
        raise HTTPException(status_code=401, detail="Wrong credentials")
    
    token = security.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}