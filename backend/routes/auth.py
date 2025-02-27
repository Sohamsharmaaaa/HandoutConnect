from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import UserCreate, Token
from backend.models import User
from backend.utils.security import hash_password, verify_password, create_access_token
from backend.crud import get_user_by_email

router = APIRouter()

# User Registration Route
@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    hashed_pwd = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_pwd, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate JWT token
    access_token = create_access_token({"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# User Login Route
@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
