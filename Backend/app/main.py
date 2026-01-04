from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AssessmentInput(BaseModel):
    stu_name: str # Student's name (string)
    course: str # Subject name (string)
    scores: float # Marks obtained (float number)


#Testing
@app.get("/")
def home():
    return {"message": "Welcome to EduMark API"}

students_db = [] #temporary list acting like a database

@app.post("/assessments/") #frontend will send data to this endpoint
def add_assessment(assessment: AssessmentInput):
    students_db.append(assessment)
    return {
        "message": "Assessment added successfully", 
        "data": assessment
    }