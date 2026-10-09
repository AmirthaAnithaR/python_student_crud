students = []
def create_student():
    id = int(input("Enter student ID: "))
    for student in students:
        if student["id"] == id:
            print("Student ID already exists!")
            return
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter department: ")
    student = {
        "id": id,
        "name": name,
        "age": age,
        "department": department
    }
    students.append(student)
    print("Student created successfully!")

def read_students():
    if not students:
        print("No students found!")
        return
    for student in students:
        print(student)


def update_student():
    id = int(input("Enter student ID to update: "))
    for student in students:
        if student["id"] == id:
            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["department"] = input("Enter new department: ")
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    id = int(input("Enter student ID to delete: "))
    for student in students:
        if student["id"] == id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")
while True:
    print("\n--- Student CRUD Application ---")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting application...")
        break
    else:
        print("Invalid choice! Try again.")
