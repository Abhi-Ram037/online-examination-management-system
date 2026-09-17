from pydantic import BaseModel


class ResultResponse(BaseModel):
    attempt_id: int
    student_id: int
    exam_id: int
    score: int
    status: str