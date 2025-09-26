from StudentManagementSystem import StudentManagementSystem, SystemInformation, AdminInformation

print(SystemInformation())


def validation(message, startIndex=None, endIndex=None) -> int:
    value = input(message)
    if value.isdigit():
        value = int(value)
        if startIndex is not None and endIndex is not None:
            if startIndex <= value <= endIndex:
                return value
            else:
                print("Value is out of range")
    else:
        print("Enter number")
    return -1

students = {
    101: {
        "student_name": "Ravi",
        "student_marks": {
            "telugu": 85,
            "hindi": 78,
            "english": 88,
            "maths": 92,
            "physics": 80,
            "chemistry": 76,
            "biology": 81,
            "social": 90
        },
        "student_skills": {"Python", "C"},
        "student_hobbies": {"Cricket", "Chess"}
    },
    102: {
        "student_name": "Sita",
        "student_marks": {
            "telugu": 90,
            "hindi": 85,
            "english": 91,
            "maths": 89,
            "physics": 87,
            "chemistry": 82,
            "biology": 84,
            "social": 86
        },
        "student_skills": {"Java", "Spring"},
        "student_hobbies": {"Reading", "Painting"}
    },
    103: {
        "student_name": "Arjun",
        "student_marks": {
            "telugu": 70,
            "hindi": 65,
            "english": 72,
            "maths": 68,
            "physics": 75,
            "chemistry": 71,
            "biology": 69,
            "social": 73
        },
        "student_skills": {"JavaScript", "Angular"},
        "student_hobbies": {"Football", "Music"}
    },
    104: {
        "student_name": "Lakshmi",
        "student_marks": {
            "telugu": 95,
            "hindi": 92,
            "english": 94,
            "maths": 96,
            "physics": 93,
            "chemistry": 90,
            "biology": 91,
            "social": 89
        },
        "student_skills": {"Data Science", "ML"},
        "student_hobbies": {"Dance", "Gardening"}
    }
}


def findStudentById(id: int) -> bool:
    if id in students:
        print("studenent_id", "->" ,id)
        for key, value in students[id].items():
            print(key, "->" , value)
        return True
    else:
        print("Id is not present in the student's data")
    return False


def listOfStudents() -> None:
    for id in students.keys():
        print("studenent_id", "->" ,id)
        for key, value in students[id].items():
            print(key, "->" ,value)


def ask_student_id(message="Enter Student Id: "):
    sid = validation(message)
    if sid < 0:
        print("Id must be a positive number")
        return None
    return sid


def add_student():
    sid = ask_student_id()
    if sid is None:
        return
    if sid in students:
        print("Id already present, please select another option")
        return

    sms = StudentManagementSystem()
    sms.student_id = sid
    sms.addStudent()

    students[sid] = {
        "student_name": sms.student_name,
        "student_marks": sms.student_marks,
        "student_skills": sms.student_skills,
        "student_hobbies": sms.student_hobbies,
    }
    print("Student added successfully")


def update_student():
    if not students:
        print("No records to update")
        return
    sid = ask_student_id()
    if sid is None:
        return
    if sid in students:
        students[sid]["student_name"] = input("Change Student Name: ")
        print("Student name updated")
    else:
        print("Id is not present")


def get_student():
    sid = ask_student_id()
    if sid and sid in students:
        for key, value in students[sid].items():
            print(key, "->", value)
    else:
        print("Student not found")


def list_students():
    if not students:
        print("No student records")
    else:
        for id in students.keys():
            print("studenent_id", id)
            for key, value in students[id].items():
                print(key, "->", value)


def delete_student():
    sid = ask_student_id()
    if sid and sid in students:
        students.pop(sid)
        print("Deleted successfully")
    else:
        print("Student not found")


actions = {
    1: add_student,
    2: update_student,
    3: get_student,
    4: list_students,
    5: delete_student,
    6: lambda: print(f"Exit the system...\n{AdminInformation()}")
}


while True:
    print("""
    1 -> Add Student
    2 -> Update Student By ID
    3 -> Get Student By ID
    4 -> Get All Students
    5 -> Delete Student By ID
    6 -> Exit the System
    """)

    choice = validation("Select 1-6: ", 1, 6)
    action = actions.get(choice)

    if action:
        action()
        if choice == 6:
            break
    else:
        print("Invalid choice, try again")
