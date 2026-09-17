from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import base


class Exam(base):

    __tablename__ = "exams"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    duration = Column(
        Integer,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    questions = relationship(
        "Question",
        back_populates="exam"
    )

    attempts = relationship(
        "ExamAttempt",
        back_populates="exam"
    )