# FastAPI Employee API

A beginner-friendly REST API built with Python and FastAPI to practice backend development fundamentals.

## Features

- Health check endpoint
- Welcome endpoint with query parameter validation
- Employee role lookup using path parameters
- HTTP error handling for employees that do not exist

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd fastapi-employee-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Explore the API

- Health check: `http://127.0.0.1:8000/health`
- Welcome: `http://127.0.0.1:8000/welcome?name=Dhanu`
- API documentation: `http://127.0.0.1:8000/docs`

## Learning Goals

- Understand REST API fundamentals
- Practice path and query parameters
- Learn request validation and HTTP error handling
- Progress toward a modular backend architecture

## Current Limitations

Employee data is stored in memory and resets when the application restarts. Database persistence, automated tests, and authentication are planned improvements.
