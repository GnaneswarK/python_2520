from Student import Student


class StudentService:
    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        if student.student_id in self.students:
            print("ID already exists")
        else:
            self.students[student.student_id] = student
            print("Student added")

    def update_student(self, sid, new_name):
        if sid in self.students:
            self.students[sid].name = new_name
            print("Updated")
        else:
            print("Not found")

    def get_student(self, sid):
        if sid in self.students:
            return self.students.get(sid)
        else:
            print("ID is not present")
            return None

    def list_students(self):
        for stu in self.students.values():
            print(stu)

    def delete_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("Deleted")
        else:
            print("Not found")
