from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.attempt import ExamAttempt


def get_all_results(db: Session):
    results = db.query(ExamAttempt).filter(
        ExamAttempt.status == "Completed"
    ).all()

    return results


def get_student_results(db: Session, student_id: int):
    results = db.query(ExamAttempt).filter(
        ExamAttempt.student_id == student_id,
        ExamAttempt.status == "Completed"
    ).all()

    return results


def get_leaderboard(db: Session):
    results = db.query(ExamAttempt).filter(
        ExamAttempt.status == "Completed"
    ).order_by(
        ExamAttempt.score.desc()
    ).all()

    leaderboard = []

    rank = 1

    for result in results:
        leaderboard.append({
            "rank": rank,
            "student_id": result.student_id,
            "exam_id": result.exam_id,
            "score": result.score
        })

        rank += 1

    return leaderboard

def filter_results(db: Session, student_id: int = None):
    query = db.query(ExamAttempt).filter(
        ExamAttempt.status == "Completed"
    )

    if student_id:
        query = query.filter(
            ExamAttempt.student_id == student_id
        )

    return query.all()

def get_results_with_pagination(
    db: Session,
    page: int,
    limit: int
):
    skip = (page - 1) * limit

    results = db.query(ExamAttempt).filter(
        ExamAttempt.status == "Completed"
    ).offset(skip).limit(limit).all()

    return results