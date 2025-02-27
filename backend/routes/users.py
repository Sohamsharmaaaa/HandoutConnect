from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import UserResponse
from backend.models import User
from backend.utils.security import create_access_token
from backend.crud import get_user_by_id
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from backend.utils.security import SECRET_KEY, ALGORITHM

router = APIRouter()

# OAuth2 scheme for protected routes
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Function to get the current authenticated user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get current user details
@router.get("/me", response_model=UserResponse)
def get_user_details(current_user: User = Depends(get_current_user)):
    return current_user

# Get all users (Admin only)
@router.get("/all", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return db.query(User).all()
