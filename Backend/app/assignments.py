from fastapi import APIRouter
from ..database import students_collection

router = APIRouter()

@router.post("/assignments")

async def add_assignment(data: dict): #async allows to database queries efficiently without blocking the server
    name = data["assignment_name"]
    marks = data["marks"]

    for student_id, mark in marks.items():
        students_collection.update_one(
            {"student_id": student_id},
            {"$set": {f"assignments.{name}": mark}}
        )

    return {"message": "Assignments added successfully"}