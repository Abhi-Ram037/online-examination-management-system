# Online Examination Management System

## Project Description

Online Examination Management System is a web-based application developed using **Python and FastAPI**. The main purpose of this project is to manage students, exams, questions, exam attempts and results in one system.

The application provides APIs for creating and managing students and exams. It also allows questions to be added to exams, students to start and submit exams, and results to be viewed.

This project was developed as a practical Python and FastAPI project to understand how REST APIs, databases, authentication and project structure work together.

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* MySQL
* JWT Authentication
* Pydantic
* Alembic
* Uvicorn

## Main Features

### Student Management

* Add a student
* View all students
* View student details
* Manage student information

### Exam Management

* Create an exam
* View exam details
* Manage active and inactive exams
* Add questions to an exam
* View questions for an exam

### Question Management

Each question contains:

* Question text
* Option A
* Option B
* Option C
* Option D
* Correct answer

Questions are connected to the respective exam.

### Exam Attempt

Students can:

* Start an exam
* Submit an exam
* Complete an exam
* Store the exam score
* View exam attempts

### Result Management

The system provides APIs to:

* View results
* View results of a particular student
* View the leaderboard

### Authentication

The project also includes login and JWT-based authentication for securing the API.

## Project Structure

```text
online-examination-management-system/
│
├── main1.py
├── database.py
├── auth.py
├── security.py
├── requirements.txt
├── alembic.ini
├── .gitignore
│
├── alembic/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── exam.py
│   ├── question.py
│   └── attempt.py
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── exam.py
│   ├── question.py
│   ├── attempt.py
│   ├── auth.py
│   └── result.py
│
├── routes/
│   ├── __init__.py
│   ├── student_routes.py
│   ├── exam_routes.py
│   ├── question_routes.py
│   ├── attempt_routes.py
│   ├── result_routes.py
│   └── auth_routes.py
│
└── services/
    ├── __init__.py
    ├── student_service.py
    ├── exam_service.py
    ├── attempt_service.py
    └── result_service.py
```

## How the Project Works

The project follows a simple layered structure.

**Routes** handle the API requests coming from the user.

**Schemas** define the request and response data using Pydantic.

**Models** define the database tables using SQLAlchemy.

**Services** contain the main business logic of the application.

**Database** handles the connection between the FastAPI application and the database.

**Authentication and Security** handle user login and JWT token-based authentication.

## Installation

First, clone the repository:

```bash
git clone https://github.com/Abhi-Ram037/online-examination-management-system.git
```

Move into the project folder:

```bash
cd online-examination-management-system
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI application using Uvicorn:

```bash
python -m uvicorn main1:app --reload
```

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI will open and all available API endpoints can be tested there.

## API Modules

The project contains APIs for:

```text
Students
Exams
Questions
Attempts
Results
Authentication
```

## Database

The application uses SQLAlchemy for database operations.

The database contains tables related to:

* Students
* Exams
* Questions
* Attempts
* Results

Alembic is included in the project for handling database migrations.

## Project Purpose

The main purpose of developing this project was to get practical experience with:

* Python programming
* FastAPI
* REST API development
* SQLAlchemy
* Database operations
* Pydantic validation
* JWT authentication
* Project folder structure
* API testing using Swagger UI
* Database migrations using Alembic

## Developer Note

This project explanation is written in a simple and straightforward developer style based on the actual project implementation. The purpose is to explain what the application does, how the files are connected, and how the API can be run and tested.

## Author

**Abhi Ram**

GitHub:
https://github.com/Abhi-Ram037
