
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from pymongo.errors import PyMongoError

import services
from schemas import StudentSchema

app = FastAPI(title="Student CRUD API")


@app.get("/")
def home():
    return {"message": "Student API is working!"}


@app.post("/students", status_code=201)
def create_student(student: StudentSchema):
    try:
        student_data = student.model_dump()

        result = services.create_student(student_data)

        if result is None:
            raise HTTPException(
                status_code=409,
                detail="Student ID already exists"
            )

        return {
            "message": "Student added successfully!",
            "student": result
        }

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Unable to save student to MongoDB"
        )


@app.get("/students")
def get_all_students():
    try:
        student_list = services.get_all_students()

        return {
            "message": "Students retrieved successfully!",
            "total": len(student_list),
            "students": student_list
        }

    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve students"
        )


@app.get("/students/{student_id}")
def get_student(student_id: int):
    try:
        student = services.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve student"
        )


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentSchema):
    try:
        if student_id != student.id:
            raise HTTPException(
                status_code=400,
                detail="Path ID and body ID must match"
            )

        student_data = student.model_dump()
        result = services.update_student(student_id, student_data)

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "message": "Student updated successfully!",
            "student": result
        }

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Unable to update student"
        )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        result = services.delete_student(student_id)

        if result == 0:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "message": "Student deleted successfully!",
            "student_id": student_id
        }

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=503,
            detail="Unable to delete student"
        )
