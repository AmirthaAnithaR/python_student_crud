
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]
students = db["students"]


def create_student():
    student_id = int(input("Enter student ID: "))

    existing_student = students.find_one({"id": student_id})

    if existing_student:
        print("Student ID already exists!")
        return

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter department: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    students.insert_one(student)

    print("Student created successfully!")


create_student()

client.close()
