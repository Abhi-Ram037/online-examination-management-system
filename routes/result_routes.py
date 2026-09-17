from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from services.result_service import (
    get_all_results,
    get_student_results,
    get_leaderboard,
    filter_results,
    get_results_with_pagination
)


router = APIRouter(
    prefix="/results",
    tags=["results"]
)


@router.get("")
def get_results(
    student_id: int = None,
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    if page < 1:
        page = 1

    if limit < 1:
        limit = 5

    if student_id:
        return filter_results(db, student_id)

    return get_results_with_pagination(
        db,
        page,
        limit
    )


@router.get("/student/{student_id}")
def get_student_result(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_student_results(db, student_id)


@router.get("/leaderboard")
def leaderboard(db: Session = Depends(get_db)):
    return get_leaderboard(db)