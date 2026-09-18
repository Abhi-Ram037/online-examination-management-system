from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import base


class ExamAttempt(base):

    __tablename__ = "exam_attempts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        index=True,
        nullable=False
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id"),
        index=True,
        nullable=False
    )

    score = Column(
        Integer,
        default=0
    )

    status = Column(
        String,
        index=True,
        default="Started"
    )

    student = relationship(
        "Student",
        back_populates="attempts"
    )

    exam = relationship(
        "Exam",
        back_populates="attempts"
    )