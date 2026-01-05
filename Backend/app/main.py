from fastapi import FastAPI
from pydantic import BaseModel
from app.database import assessments_collection
from bson import ObjectId
from typing import List
import json

app = FastAPI()

# Pydantic model
class AssessmentInput(BaseModel):
    stu_name: str # Student's name (string)
    course: str # Subject name (string)
    scores: float # Marks obtained (float number)


#Helper function to convert MongoDB docu to JSON
def assessment_helper(assessment) -> dict:
    return {
        "id": str(assessment["_id"]),
        "stu_name": assessment["stu_name"],
        "course": assessment["course"],
        "scores": assessment["scores"],
    }



#Testing
@app.get("/")
def home():
    return {"message": "Welcome to EduMark API"}

#students_db = [] #temporary list acting like a database
#now that we don't need this, we can comment it out for future reference


#POST /assessments/ : Add a new assessment
@app.post("/assessments/") #frontend will send data to this endpoint
async def add_assessment(assessment: AssessmentInput):
    assessment_dict = assessment.dict()
    result = await assessments_collection.insert_one(assessment_dict)
    new_assessment = await assessments_collection.find_one({"_id": result.inserted_id})
    return {
        "message": "Assessment added successfully",
        "assessment": assessment_helper(new_assessment)
    }

#GET all assessments
@app.get("/assessments/", response_model=List[AssessmentInput])
async def get_assessments():
    assessments = []
    async for assessment in assessments_collection.find():
        assessments.append(assessment_helper(assessment))
    return assessments