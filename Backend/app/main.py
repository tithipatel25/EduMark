from fastapi import FastAPI
from app.routes import upload, classes

app = FastAPI(title = "EduMark API")

app.include_router(upload.router, prefix="/upload")
app.include_router(classes.router, prefix="/classes")