from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas import UserResponse
from backend.models import Donation, User
from backend.routes.users import get_current_user
from backend.schemas import DonationCreate, DonationResponse, DonationUpdate

router = APIRouter()

# Create a donation request (Institute only)
@router.post("/", response_model=DonationResponse)
def create_donation(donation: DonationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "institute":
        raise HTTPException(status_code=403, detail="Only institutes can request donations")

    new_donation = Donation(
        donor_id=None,  # No donor yet
        institute_id=current_user.id,
        item_name=donation.item_name,
        quantity=donation.quantity,
        status="pending"
    )
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)
    return new_donation

# Get all donation requests (For donors)
@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
    return db.query(Donation).filter(Donation.status == "pending").all()

# Update donation status (Only institutes can mark as completed)
@router.put("/{donation_id}", response_model=DonationResponse)
def update_donation_status(donation_id: int, update_data: DonationUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")

    if donation.institute_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this donation")

    donation.status = update_data.status
    db.commit()
    db.refresh(donation)
    return donation
