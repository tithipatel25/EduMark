from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from .routes.upload import router as upload_router
from .routes.students import router as students_router
from app.routes import assignments

app = FastAPI()

app.include_router(assignments.router, prefix ="/api") 

#allows frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True, # Allows cookies to be sent
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(upload_router, prefix="/api")
app.include_router(students_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the EduMark API! Backend is running."}