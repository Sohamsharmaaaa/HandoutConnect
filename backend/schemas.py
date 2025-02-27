from pydantic import BaseModel

# User Schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "donor"  # Default role is "donor"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to be converted to Pydantic models

# Token Schema for Authentication
class Token(BaseModel):
    access_token: str
    token_type: str

# Create a donation request
class DonationCreate(BaseModel):
    item_name: str
    quantity: int

# Response model for donations
class DonationResponse(BaseModel):
    id: int
    donor_id: int | None
    institute_id: int
    item_name: str
    quantity: int
    status: str

    class Config:
        orm_mode = True

# Update donation status
class DonationUpdate(BaseModel):
    status: str

