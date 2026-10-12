
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=3000
)

db = client["student_db"]
students_collection = db["students"]
