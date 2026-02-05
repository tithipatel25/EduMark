from pymongo import MongoClient #allows you to connect with the database
import os
from dotenv import load_dotenv #load varibles from .env file 

load_dotenv() #load the .env file

MONGO_URL = os.getenv("MONGO_URL") 

client = MongoClient(MONGO_URL)
db = client.edumark #database name

classes_collection = db.classes

