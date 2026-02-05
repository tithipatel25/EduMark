from pymongo import MongoClient #allows you to connect with the database

client = MongoClient("mongodb://localhost:27017") 
db = client.edumark

students_collection = db.students

