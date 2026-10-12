
import repository


def create_student(student_data):
    existing_student = repository.get_student_by_id(
        student_data["id"]
    )

    if existing_student:
        return None

    return repository.create_student(student_data)


def get_all_students():
    return repository.get_all_students()


def get_student_by_id(student_id):
    return repository.get_student_by_id(student_id)


def update_student(student_id, student_data):
    existing_student = repository.get_student_by_id(student_id)

    if not existing_student:
        return None

    repository.update_student(student_id, student_data)
    return repository.get_student_by_id(student_id)


def delete_student(student_id):
    return repository.delete_student(student_id)
