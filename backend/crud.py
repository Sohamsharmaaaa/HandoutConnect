from sqlalchemy.orm import Session
from backend.models import User
from backend.utils.security import hash_password

# Create a new user
def create_user(db: Session, name: str, email: str, password: str, role: str):
    hashed_pwd = hash_password(password)
    new_user = User(name=name, email=email, hashed_password=hashed_pwd, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
