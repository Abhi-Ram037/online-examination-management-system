from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import base


class Student(base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    attempts = relationship(
        "ExamAttempt",
        back_populates="student"
    )