from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import admin_required
from schemas.exam import ExamCreate
from schemas.question import QuestionCreate

from services.exam_service import (
    create_exam,
    get_all_exams,
    get_exam,
    add_question,
    get_exam_questions,
    get_exams_with_pagination
)


router = APIRouter(
    prefix="/exams",
    tags=["exams"]
)


@router.get("")
def get_exams(
    category: str = None,
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    if page < 1:
        page = 1

    if limit < 1:
        limit = 5

    if category:
        from services.exam_service import filter_exams
        return filter_exams(db, category)

    return get_exams_with_pagination(
        db,
        page,
        limit
    )


@router.post("")
def add_exam(
    exam_data: ExamCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(admin_required)
):
    return create_exam(db, exam_data)


@router.post("/questions")
def add_exam_question(
    question_data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(admin_required)
):
    return add_question(db, question_data)


@router.get("/{exam_id}/questions")
def get_questions(
    exam_id: int,
    db: Session = Depends(get_db)
):
    return get_exam_questions(db, exam_id)


@router.get("/{exam_id}")
def get_exam_by_id(
    exam_id: int,
    db: Session = Depends(get_db)
):
    return get_exam(db, exam_id)