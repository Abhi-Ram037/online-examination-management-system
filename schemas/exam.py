from pydantic import BaseModel, Field


class ExamCreate(BaseModel):
    title: str = Field(min_length=1)
    category: str = Field(min_length=1)
    duration: int = Field(gt=0)
    is_active: bool = True