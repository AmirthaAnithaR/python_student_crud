
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    db = client["student_db"]
    print("Database selected:", db.name)

except Exception as e:
    print("MongoDB connection failed:", e)

finally:
    client.close()
