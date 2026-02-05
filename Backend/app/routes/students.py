from fastapi import APIRouter
from ..database import students_collection

router = APIRouter()

@router.get("/students")
def get_students():
    return list(students_collection.find({}, {"_id":0})) #returns all student documents excluding the MongoDB-generated _id field