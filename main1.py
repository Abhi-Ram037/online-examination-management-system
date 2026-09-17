from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import base, engine

from models.student import Student
from models.exam import Exam
from models.question import Question
from models.attempt import ExamAttempt

from routes.student_routes import router as student_router
from routes.exam_routes import router as exam_router
from routes.attempt_routes import router as attempt_router
from routes.result_routes import router as result_router
from routes.auth_routes import router as auth_router


base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Online Examination Management System",
    description="FastAPI Online Examination Management System",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(student_router)
app.include_router(exam_router)
app.include_router(attempt_router)
app.include_router(result_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "online examination management system is running"
    }