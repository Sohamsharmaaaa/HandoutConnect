from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="donor")  # donor, institute, supplier
    is_active = Column(Boolean, default=True)

    donations = relationship("Donation", back_populates="donor")

# Donation Model
class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer, ForeignKey("users.id"))
    institute_id = Column(Integer, ForeignKey("users.id"))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String, default="pending")  # pending, completed

    donor = relationship("User", foreign_keys=[donor_id], back_populates="donations")
    institute = relationship("User", foreign_keys=[institute_id])
