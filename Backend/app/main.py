from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str # Student's name (string)
    subject: str # Subject name (string)
    marks: float # Marks obtained (float number)


#Testing
@app.get("/")
def home():
    return {"message": "Welcome to the Student Marks API"}


students_db = [] #temporary list acting like a database

@app.post("/add_mark/") #frontend will send data to this endpoint
def add_mark(student: Student): #FastAPI will automatically read the incoming JSON to Student model
    students_db.append(student)
    return {"message": "Student marks added successfully", "data": student}