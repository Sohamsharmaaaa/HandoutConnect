from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    # ✅ Fix ForeignKey Reference
    donations = relationship("Donation", back_populates="user", foreign_keys="Donation.user_id")

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # ✅ Correct ForeignKey
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    # ✅ Fix ForeignKey Reference
    user = relationship("User", back_populates="donations", foreign_keys=[user_id])
