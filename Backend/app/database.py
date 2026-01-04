from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017" 

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.edumark #database name
assessments_collection = db.get_collection("assessments") #collection for storing assessment data