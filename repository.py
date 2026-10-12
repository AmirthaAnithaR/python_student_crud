
from database import students_collection


def create_student(student_data):
    students_collection.insert_one(student_data)
    return student_data


def get_all_students():
    return list(students_collection.find({}, {"_id": 0}))


def get_student_by_id(student_id):
    return students_collection.find_one(
        {"id": student_id},
        {"_id": 0}
    )


def update_student(student_id, student_data):
    result = students_collection.update_one(
        {"id": student_id},
        {"$set": student_data}
    )
    return result.matched_count


def delete_student(student_id):
    result = students_collection.delete_one({"id": student_id})
    return result.deleted_count
