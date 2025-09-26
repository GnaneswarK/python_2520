from StudentManagementSystem import StudentManagementSystem, SystemInformation, AdminInformation

print(SystemInformation())


def validation(message, startIndex=None, endIndex=None) -> int:
    value = input(message)
    if value.isdigit():
        value = int(value)
        # Check range only if startIndex and endIndex are given
        if startIndex is not None and endIndex is not None:
            if startIndex <= value <= endIndex:
                return value
            else:
                return -1
        return value
    else:
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
# MENU CARD


def findStudentById(id: int) -> bool:
    if id in students:
        print("studenent_id", id)
        for [key, value] in students[id].items():
            print(key, value)
        return True
    else:
        print("Id is not present in the student's data")
    return False


def listOfStudents() -> None:
    for id in students.keys():
        print("studenent_id", id)
        for [key, value] in students[id].items():
            print(key, value)


while True:
    print(f"What type of action you need to perform\n"
          f"1 -> Add Student\n"
          f"2 -> Update Student By ID\n"
          f"3 -> Get Student By ID\n"
          f"4 -> Get All Students\n"
          f"5 -> Delete student By ID\n"
          f"6 -> Exit the System")
    action = validation("Select 1-6 : ", 1, 6)
    if action:
        match (action):
            case 1:
                while True:
                    student_id = validation("Enter Student Id : ")
                    if student_id < 0:
                        print("Id must be positive number and in between ")
                    else:
                        if not student_id in students:
                            student_management_system: StudentManagementSystem = StudentManagementSystem()
                            student_management_system.student_id = student_id
                            student_management_system.addStudent()
                            student = {}
                            student[student_id] = {
                                "student_name": student_management_system.student_name,
                                "student_marks": student_management_system.student_marks,
                                "student_skills": student_management_system.student_skills,
                                "student_hobbies": student_management_system.student_hobbies
                            }
                            students.update(student)
                        else:
                            print(
                                "Id already present please select appropraite option")
                        break
            case 2:
                while True:
                    if not students:
                        print("No reocrds to perform action")
                        break
                    student_id = validation("Enter Student Id : ")
                    if student_id < 0:
                        print("Id must be positive number ")
                    else:
                        if student_id in students:
                            student_name = input("Change Student Name :")
                            students[student_id]["student_name"] = student_name
                            print("Student name updated")
                        else:
                            print("Id is not present please re check it")
                        break

            case 3:
                while True:
                    student_id = validation("Enter Student Id : ")
                    if student_id < 0:
                        print("Id must be positive number ")
                    else:
                        status = findStudentById(student_id)
                    if status:
                        break

            case 4:
                print("FUll Student lists")
                listOfStudents()
            case 5:
                while True:
                    if not students:
                        print("No records to perfrom action")
                        break
                    student_id = validation("Enter Student Id : ")
                    if student_id < 0:
                        print("Id must be positive number and in between ")
                    else:
                        if student_id in students:
                            students.pop(student_id)
                            print("Succesfully deleted the record")
                        else:
                            print("Id is not present please re check it")
                        break
            case 6:
                print("Terminated the student management system")
                print(AdminInformation())
                break
            case _:
                print("Invalid Number")
