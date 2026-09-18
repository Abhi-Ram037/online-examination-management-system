# Online Examination Management System

A REST API-based **Online Examination Management System** developed using **Python and FastAPI**. The application provides APIs for student management, exam management, question management, exam attempts, result calculation, authentication, and leaderboard management.

The project follows a modular backend structure using **FastAPI, SQLAlchemy, Pydantic, SQLite, JWT authentication, and Alembic**.

---

## 🚀 Features

* Student registration and management
* Create and manage examinations
* Add questions to examinations
* View examination questions
* Start an examination
* Submit examination attempts
* Automatic score calculation
* Manage examination attempts
* View all results
* View student-wise results
* View examination leaderboard
* User login and authentication
* JWT token-based authentication
* Password hashing
* Input validation using Pydantic
* Database operations using SQLAlchemy
* Database migrations using Alembic
* Interactive API documentation using Swagger UI
* ReDoc API documentation

---

## 🛠️ Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Backend programming           |
| FastAPI    | REST API framework            |
| SQLAlchemy | ORM and database operations   |
| Pydantic   | Data validation               |
| SQLite     | Database                      |
| Alembic    | Database migrations           |
| JWT        | Authentication                |
| Passlib    | Password hashing              |
| Uvicorn    | Application server            |
| Swagger UI | API testing and documentation |

---

## 📁 Project Structure

```text
online_examination/
│
├── alembic/
│   ├── README
│   ├── env.py
│   └── script.py.mako
│
├── models/
│   ├── student.py
│   ├── exam.py
│   ├── question.py
│   └── attempt.py
│
├── schemas/
│   ├── student.py
│   ├── exam.py
│   ├── question.py
│   └── attempt.py
│
├── services/
│   ├── student_service.py
│   ├── exam_service.py
│   └── attempt_service.py
│
├── routes/
│   ├── student_routes.py
│   ├── exam_routes.py
│   ├── question_routes.py
│   └── attempt_routes.py
│
├── auth.py
├── database.py
├── security.py
├── main1.py
├── alembic.ini
├── requirements.txt
└── .gitignore
```

---

## 🧩 Project Architecture

The project is divided into different layers to keep the code organized and easier to maintain.

```text
                    Client
                      │
                      ▼
                FastAPI Routes
                      │
                      ▼
                   Schemas
                      │
                      ▼
                  Services
                      │
                      ▼
                    Models
                      │
                      ▼
                  SQLAlchemy
                      │
                      ▼
                   SQLite
```

### Routes

The `routes` folder contains the API endpoints for students, exams, questions, and exam attempts.

### Schemas

The `schemas` folder contains Pydantic models used for request validation and response data.

### Services

The `services` folder contains the main business logic of the application.

### Models

The `models` folder contains SQLAlchemy database models and defines the database structure and relationships.

### Database

The `database.py` file contains the database connection and SQLAlchemy configuration.

### Authentication

The `auth.py` and `security.py` files handle authentication, password protection, and JWT-related functionality.

---

# 📚 API Endpoints

## 👨‍🎓 Student APIs

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| GET    | `/students`              | Get all students     |
| POST   | `/students`              | Create a new student |
| GET    | `/students/{student_id}` | Get student by ID    |

---

## 📝 Exam APIs

| Method | Endpoint                     | Description               |
| ------ | ---------------------------- | ------------------------- |
| GET    | `/exams`                     | Get all exams             |
| POST   | `/exams`                     | Create a new exam         |
| GET    | `/exams/{exam_id}`           | Get exam by ID            |
| POST   | `/exams/questions`           | Add a question            |
| GET    | `/exams/{exam_id}/questions` | Get questions for an exam |

---

## 📋 Attempt APIs

| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| POST   | `/attempts/start`  | Start an examination         |
| POST   | `/attempts/submit` | Submit an examination        |
| GET    | `/attempts`        | Get all examination attempts |

---

## 🏆 Result APIs

| Method | Endpoint                        | Description                 |
| ------ | ------------------------------- | --------------------------- |
| GET    | `/results`                      | Get all results             |
| GET    | `/results/student/{student_id}` | Get results for a student   |
| GET    | `/results/leaderboard`          | Get examination leaderboard |

---

## 🔐 Authentication API

| Method | Endpoint | Description                             |
| ------ | -------- | --------------------------------------- |
| POST   | `/login` | Login and generate authentication token |

---

# 🔄 Application Workflow

```text
                  Student
                     │
                     ▼
              Student Registration
                     │
                     ▼
                   Login
                     │
                     ▼
               View Available Exams
                     │
                     ▼
                 Start Exam
                     │
                     ▼
               Answer Questions
                     │
                     ▼
                Submit Exam
                     │
                     ▼
              Calculate Score
                     │
                     ▼
                View Result
                     │
                     ▼
                 Leaderboard
```

---

# 🗄️ Database Relationships

The application contains relationships between students, exams, questions, and attempts.

```text
Student
   │
   │ 1
   │
   └──────────────< Many
                  Exam Attempts
                       │
                       │
                       ▼
                     Exam


Exam
 │
 │ 1
 │
 └──────────────< Many
                Questions
```

### Main Relationships

* One student can have multiple exam attempts.
* One exam can contain multiple questions.
* An exam attempt connects a student with an exam.
* Exam results are generated based on submitted attempts.

---

# 🔑 Authentication

The application includes authentication using **JWT tokens**.

The general authentication process is:

```text
User Login
    ↓
Validate Credentials
    ↓
Password Verification
    ↓
Generate JWT Token
    ↓
Authenticated API Access
```

Passwords are protected using password hashing instead of storing plain-text passwords.

---

# 🧪 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to:

* View available APIs
* Enter request parameters
* Send API requests
* Check responses
* Test authentication
* Understand request and response schemas

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/online-examination.git
```

Move into the project directory:

```bash
cd online-examination
```

---

## 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🗃️ Database Setup

The application uses **SQLite** for local database storage.

Database configuration is handled through:

```text
database.py
```

Alembic is included for database migration management.

To apply existing migrations:

```bash
alembic upgrade head
```

To create a new migration after changing database models:

```bash
alembic revision --autogenerate -m "update database"
```

Then apply the migration:

```bash
alembic upgrade head
```

---

# 🔐 Environment Variables

Create a `.env` file in the project directory for secret configuration values.

Example:

```text
secret_key=your_secret_key
```

**Do not upload your `.env` file to GitHub.**

The project `.gitignore` file already prevents `.env` from being tracked.

---

# ▶️ Running the Application

Start the FastAPI application using:

```bash
python -m uvicorn main1:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing the Application

The APIs can be tested directly through Swagger UI.

### Basic testing flow

```text
1. Start the application
        ↓
2. Open /docs
        ↓
3. Create a student
        ↓
4. Create an exam
        ↓
5. Add questions
        ↓
6. Start an exam attempt
        ↓
7. Submit the exam
        ↓
8. Check the result
        ↓
9. Check the leaderboard
```

---

# 📦 Dependencies

The project dependencies are stored in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

Main dependencies include:

```text
FastAPI
SQLAlchemy
Pydantic
Alembic
Uvicorn
Passlib
Python-JOSE
Python-Dotenv
```

---

# 🛡️ Security

The project includes basic backend security practices such as:

* JWT authentication
* Password hashing
* Request validation
* Protected configuration using environment variables
* Separation of authentication and application logic

Secret values should always be stored in environment variables rather than directly inside source code.

---

# 📈 Learning Outcomes

This project helped me practice:

* Python programming
* FastAPI development
* REST API development
* CRUD operations
* SQLAlchemy ORM
* Pydantic validation
* SQLite database management
* Database relationships
* JWT authentication
* Password hashing
* API routing
* Service-layer architecture
* Alembic database migrations
* Swagger API testing
* Backend project structure

---

# 🚀 Future Improvements

The application can be extended with:

* Admin dashboard
* Role-based access control
* Examination timer
* Question randomization
* Multiple-choice question categories
* Pagination
* Email notifications
* Detailed student performance reports
* Frontend application
* Cloud database
* Cloud deployment
* Automated testing

---

# 💻 How the Project Works

The application follows a layered backend approach.

A request first reaches the **FastAPI route**. The request data is validated using **Pydantic schemas**. The route then communicates with the **service layer**, where the application's business logic is handled. The service layer interacts with the **SQLAlchemy models**, which communicate with the SQLite database. The processed result is then returned to the client through the FastAPI API.

This structure keeps the application organized by separating API routes, validation, business logic, and database operations.

---

# 📸 Screenshots

Screenshots of the Swagger API documentation can be added here.

Example:

```text
screenshots/
├── students.png
├── exams.png
├── questions.png
├── attempts.png
└── results.png
```

Add screenshots after taking them from:

```text
http://127.0.0.1:8000/docs
```

---

# 👨‍💻 Author

**Abhiram**

Python / FastAPI Developer

This project was developed as a backend learning project to practice Python, FastAPI, REST APIs, databases, authentication, and backend application development.

---

# ⭐ Project

If you find this project useful, you can give the repository a star on GitHub.

---

## 📄 License

This project is created for learning and educational purposes.
