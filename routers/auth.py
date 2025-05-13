from fastapi import APIRouter, HTTPException
from models.user import User
from database import db
import bcrypt

router = APIRouter()

@router.post("/register")
def register_user(user: User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    db.users.insert_one({"email": user.email, "password": hashed_pw, "role": user.role})
    return {"message": "User registered successfully"}
