from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.attempt import AttemptStart, AttemptSubmit

from services.attempt_service import (
    start_attempt,
    submit_attempt,
    get_attempt,
    filter_attempts
)


router = APIRouter(
    prefix="/attempts",
    tags=["attempts"]
)


@router.post("/start")
def start_exam_attempt(
    attempt_data: AttemptStart,
    db: Session = Depends(get_db)
):
    return start_attempt(db, attempt_data)


@router.post("/submit")
def submit_exam_attempt(
    attempt_data: AttemptSubmit,
    db: Session = Depends(get_db)
):
    return submit_attempt(db, attempt_data)


@router.get("")
def get_attempts(
    status: str = None,
    db: Session = Depends(get_db)
):
    return filter_attempts(db, status)