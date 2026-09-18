from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.student import Student
from schemas.student import StudentCreate
from models.attempt import ExamAttempt
from models.exam import Exam


def create_student(
    db: Session,
    student_data: StudentCreate
):

    old_student = db.query(Student).filter(
        Student.email == student_data.email
    ).first()

    if old_student:
        raise HTTPException(
            status_code=400,
            detail="email already registered"
        )

    student = Student(
        name=student_data.name,
        email=student_data.email
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_all_students(db: Session):

    students = db.query(Student).all()

    return students


def get_student(
    db: Session,
    student_id: int
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    return student

def get_students_with_pagination(
    db: Session,
    page: int,
    limit: int
):
    skip = (page - 1) * limit

    students = db.query(Student).offset(skip).limit(limit).all()

    return students

def get_student_exams(db: Session, student_id: int):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    exams = db.query(Exam).join(
        ExamAttempt,
        Exam.id == ExamAttempt.exam_id
    ).filter(
        ExamAttempt.student_id == student_id
    ).all()

    return exams