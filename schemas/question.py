from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    question_text: str = Field(min_length=1)

    option_a: str = Field(min_length=1)
    option_b: str = Field(min_length=1)
    option_c: str = Field(min_length=1)
    option_d: str = Field(min_length=1)

    correct_answer: str = Field(min_length=1)

    exam_id: int