from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.exam import Exam
from models.question import Question

from schemas.exam import ExamCreate
from schemas.question import QuestionCreate


def create_exam(
    db: Session,
    exam_data: ExamCreate
):

    if exam_data.duration <= 0:
        raise HTTPException(
            status_code=400,
            detail="duration must be greater than 0"
        )

    exam = Exam(
        title=exam_data.title,
        category=exam_data.category,
        duration=exam_data.duration,
        is_active=exam_data.is_active
    )

    db.add(exam)
    db.commit()
    db.refresh(exam)

    return exam


def get_all_exams(db: Session):

    exams = db.query(Exam).all()

    return exams


def get_exam(
    db: Session,
    exam_id: int
):

    exam = db.query(Exam).filter(
        Exam.id == exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="exam not found"
        )

    return exam


def add_question(
    db: Session,
    question_data: QuestionCreate
):

    exam = db.query(Exam).filter(
        Exam.id == question_data.exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="exam not found"
        )

    correct_answer = question_data.correct_answer.lower()

    if correct_answer not in ["a", "b", "c", "d"]:
        raise HTTPException(
            status_code=400,
            detail="correct answer must be a, b, c or d"
        )

    question = Question(
        question_text=question_data.question_text,
        option_a=question_data.option_a,
        option_b=question_data.option_b,
        option_c=question_data.option_c,
        option_d=question_data.option_d,
        correct_answer=correct_answer,
        exam_id=question_data.exam_id
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question


def get_exam_questions(
    db: Session,
    exam_id: int
):

    exam = db.query(Exam).filter(
        Exam.id == exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="exam not found"
        )

    questions = db.query(Question).filter(
        Question.exam_id == exam_id
    ).all()

    return questions

def filter_exams(db: Session, category: str = None):
    query = db.query(Exam)

    if category:
        query = query.filter(
            Exam.category == category
        )

    return query.all()

def get_exams_with_pagination(
    db: Session,
    page: int,
    limit: int
):
    skip = (page - 1) * limit

    exams = db.query(Exam).offset(skip).limit(limit).all()

    return exams