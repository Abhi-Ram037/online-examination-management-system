from pydantic import BaseModel


class AttemptStart(BaseModel):
    student_id: int
    exam_id: int


class Answer(BaseModel):
    question_id: int
    answer: str


class AttemptSubmit(BaseModel):
    attempt_id: int
    answers: list[Answer]