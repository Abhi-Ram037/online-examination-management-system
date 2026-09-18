from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.student import StudentCreate
from services.student_service import (
    create_student,
    get_all_students,
    get_student,
    get_students_with_pagination,
    get_student_exams
)


router = APIRouter(
    prefix="/students",
    tags=["students"]
)


@router.get("")
def get_students(
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    if page < 1:
        page = 1

    if limit < 1:
        limit = 5

    return get_students_with_pagination(
        db,
        page,
        limit
    )


@router.post("")
def add_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student_data)


@router.get("/{student_id}")
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_student(db, student_id)

@router.get("/{student_id}/exams")
def get_student_exam_list(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_student_exams(db, student_id)


@router.get("/{student_id}")
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    return get_student(db, student_id)