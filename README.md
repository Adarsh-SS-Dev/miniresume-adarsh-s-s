# Mini Resume Collector API

## Python Version Used
Python 3.10+

## Installation

1. Clone repository
2. Create virtual environment
3. Install requirements:

pip install -r requirements.txt

## Run Application

uvicorn main:app --reload

Visit:
http://127.0.0.1:8000/docs

## Example API Request

POST /resumes

{
  "full_name": "Adarsh",
  "email": "adarsh@gmail.com",
  "phone": "7012924619",
  "skills": ["Python"],
  "experience_years": 3
}

Response:

{
  "id": "uuid",
  "full_name": "Adarsh",
  "email": "adarsh@gmail.com",
  "phone": "7012924619",
  "skills": ["Python"],
  "experience_years": 3
}
