from fastapi import APIRouter
from ..database import students_collection

router = APIRouter()

@router.get("/students")
def get_students():
    students = list(students_collection.find({}, {"_id": 0})) # Retrieves all student records from the MongoDB collection, excluding the "_id" field
    return students