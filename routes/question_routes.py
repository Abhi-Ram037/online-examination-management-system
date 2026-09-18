from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import admin_required
from schemas.question import QuestionCreate

from services.exam_service import add_question


router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)


@router.post("")
def add_question_route(
    question_data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(admin_required)
):
    return add_question(db, question_data)