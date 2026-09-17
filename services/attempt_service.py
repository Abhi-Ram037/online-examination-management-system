from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.student import Student
from models.exam import Exam
from models.question import Question
from models.attempt import ExamAttempt

from schemas.attempt import AttemptStart, AttemptSubmit


def start_attempt(
    db: Session,
    attempt_data: AttemptStart
):

    student = db.query(Student).filter(
        Student.id == attempt_data.student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    exam = db.query(Exam).filter(
        Exam.id == attempt_data.exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="exam not found"
        )

    if not exam.is_active:
        raise HTTPException(
            status_code=400,
            detail="exam is not active"
        )

    questions = db.query(Question).filter(
        Question.exam_id == exam.id
    ).all()

    if len(questions) < 5:
        raise HTTPException(
            status_code=400,
            detail="exam must have at least 5 questions"
        )

    old_attempt = db.query(ExamAttempt).filter(
        ExamAttempt.student_id == student.id,
        ExamAttempt.exam_id == exam.id
    ).first()

    if old_attempt:
        raise HTTPException(
            status_code=400,
            detail="student has already attempted this exam"
        )

    attempt = ExamAttempt(
        student_id=student.id,
        exam_id=exam.id,
        score=0,
        status="Started"
    )

    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return attempt


def submit_attempt(
    db: Session,
    attempt_data: AttemptSubmit
):

    attempt = db.query(ExamAttempt).filter(
        ExamAttempt.id == attempt_data.attempt_id
    ).first()

    if not attempt:
        raise HTTPException(
            status_code=404,
            detail="attempt not found"
        )

    if attempt.status == "Completed":
        raise HTTPException(
            status_code=400,
            detail="attempt already submitted"
        )

    questions = db.query(Question).filter(
        Question.exam_id == attempt.exam_id
    ).all()

    if len(attempt_data.answers) != len(questions):
        raise HTTPException(
            status_code=400,
            detail="all questions must be answered"
        )

    score = 0

    for answer in attempt_data.answers:

        question = db.query(Question).filter(
            Question.id == answer.question_id,
            Question.exam_id == attempt.exam_id
        ).first()

        if not question:
            raise HTTPException(
                status_code=400,
                detail="invalid question"
            )

        user_answer = answer.answer.lower()

        if user_answer == question.correct_answer.lower():
            score += 1

    attempt.score = score
    attempt.status = "Completed"

    db.commit()
    db.refresh(attempt)

    return attempt


def get_attempt(
    db: Session,
    attempt_id: int
):

    attempt = db.query(ExamAttempt).filter(
        ExamAttempt.id == attempt_id
    ).first()

    if not attempt:
        raise HTTPException(
            status_code=404,
            detail="attempt not found"
        )

    return attempt

def filter_attempts(db: Session, status: str = None):
    query = db.query(ExamAttempt)

    if status:
        query = query.filter(
            ExamAttempt.status == status
        )

    return query.all()