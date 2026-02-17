from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import List
from uuid import uuid4

app = FastAPI()


resumes = []


class Resume(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    skills: List[str]
    experience_years: int = Field(..., ge=0)

class ResumeResponse(Resume):
    id: str


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}


@app.post("/resumes", response_model=ResumeResponse, status_code=status.HTTP_201_CREATED)
def create_resume(resume: Resume):
    resume_id = str(uuid4())
    resume_data = resume.dict()
    resume_data["id"] = resume_id
    resumes.append(resume_data)
    return resume_data


@app.get("/resumes", response_model=List[ResumeResponse])
def get_resumes():
    return resumes


@app.get("/resumes/{resume_id}", response_model=ResumeResponse)
def get_resume(resume_id: str):
    for resume in resumes:
        if resume["id"] == resume_id:
            return resume

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Resume not found"
    )
