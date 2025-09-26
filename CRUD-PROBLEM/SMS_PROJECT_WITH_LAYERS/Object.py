from StudentService import StudentService
from Student import Student

def main():
    service = StudentService()

    while True:
        print("""
        1 -> Add Student
        2 -> Update Student By ID
        3 -> Get Student By ID
        4 -> Get All Students
        5 -> Delete Student By ID
        6 -> Exit the System
        """)

        choice = int(input("Enter choice: "))
        
        if choice == 1:
            sid = int(input("ID: "))
            name = input("Name: ")
            student = Student(sid, name)
            service.add_student(student)

        elif choice == 2:
            sid = int(input("ID: "))
            name = input("New Name: ")
            service.update_student(sid, name)

        elif choice == 3:
            sid = int(input("ID: "))
            stu = service.get_student(sid)
            print(stu if stu else "Not found")

        elif choice == 4:
            service.list_students()

        elif choice == 5:
            sid = int(input("ID: "))
            service.delete_student(sid)

        elif choice == 6:
            print("Goodbye!")
            break