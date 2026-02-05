from fastapi import APIRouter, UploadFile, File, HTTPException
from ..database import students_collection
from ..utils.parser import parse_txt

router = APIRouter()

@router.post("/upload")
async def upload_txt(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are allowed.")
    
    content = await file.read() #reads the content of the uploaded file
    text = content.decode("utf-8") #decodes the content from bytes to string using UTF-8 encoding

    students = parse_txt(text) #parses the text content to extract student data

    if not students:
        raise HTTPException(status_code=400, detail="No valid students found.")
    
    students_collection.delete_many({}) # Clear existing data
    students_collection.insert_many(students) # Inserts the parsed student data into the MongoDB collection

    return {
        "message": "File uploaded successfully",
        "students_count": len(students)
    }