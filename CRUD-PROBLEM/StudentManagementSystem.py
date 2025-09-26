#   SYSTEM INFO
class SystemInformation:
    def __init__(self):
        self.COLEEGE_NAME = "Presidency University"
        self.SOFTWARE_NAME = "Student Management sytem"
        self.VERSION_ID = "1.0.3"

    def __str__(self) -> str:
        return f"college name : {self.COLEEGE_NAME}\nsoftware Name : {self.SOFTWARE_NAME}\nversion Id : {self.VERSION_ID}"


class AdminInformation:
    def __init__(self):
        self.CONTACT_NUMBER = 40529999
        self.EMAIL_ID = "admin.presidencyuniversity.in"

    def __str__(self):
        return f"Contact number : {self.CONTACT_NUMBER}\nEmail ID : {self.EMAIL_ID}"


class StudentManagementSystem:
    def __init__(self):
        self._student_id: int = None
        self._student_name: str = None
        self._student_marks: dict = dict()
        self._student_skills: set = set()
        self._student_hobbies: set = set()

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, sid: int):
        if not isinstance(sid, int):
            raise ValueError("ID must be an integer")
        self._student_id = sid

    # Name
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self._student_name = name

    @property
    def student_marks(self):
        return self._student_marks

    @student_marks.setter
    def student_marks(self, marks: dict):
        if not isinstance(marks, dict):
            raise ValueError("Marks must be a dictionary")
        self._student_marks = marks

    @property
    def student_skills(self):
        return self._student_skills

    @student_skills.setter
    def student_skills(self, skills: set):
        if not isinstance(skills, set):
            raise ValueError("Skills must be a set")
        self._student_skills = skills

    @property
    def student_hobbies(self):
        return self._student_hobbies

    @student_hobbies.setter
    def student_hobbies(self, hobbies: set):
        if not isinstance(hobbies, set):
            raise ValueError("Hobbies must be a set")
        self._student_hobbies = hobbies

    def addStudent(self):
        self.student_name = input("Enter student Name : ").title()
        print("Enter student marks subject wise")
        self.student_marks["telugu"] = self.__addMarks("telugu")
        self.student_marks["hindi"] = self.__addMarks("Hindi")
        self.student_marks["english"] = self.__addMarks("English")
        self.student_marks["maths"] = self.__addMarks("Maths")
        self.student_marks["physics"] = self.__addMarks("Physics")
        self.student_marks["chemistry"] = self.__addMarks("Chemistry")
        self.student_marks["biology"] = self.__addMarks("Biology")
        self.student_marks["social"] = self.__addMarks("Social")
        self.__addSkills()
        self.__addhobbies()

    def __addSkills(self) -> None:
        print(f"1 -> add skills 2 -> Done Adding skills ")
        self.__skills_and_hobbiles_validation(
            "Enter your choice ", 1, 2, self.student_skills)

    def __addhobbies(self) -> None:
        print(f"1 -> add hobbies 2 -> Done Adding hobbies ")
        self.__skills_and_hobbiles_validation(
            "Enter your choice ", 1, 2, self.student_hobbies)

    def __number_validation(self, message) -> int:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            return -1

    def __skills_and_hobbiles_validation(self, message, startIndex, endIndex, skillsAndHobiles) -> None:
        value = input(message)
        if value.isdigit() and startIndex <= int(value) <= endIndex:
            if int(value) == startIndex:
                if skillsAndHobiles is self._student_skills:
                    type_name = "Skills"
                else:
                    type_name = "Hobbies"
                skillsAndHobiles.add(input(f"Add {type_name} : ").title())
            elif int(value) == endIndex:
                return
        else:
            print(
                f"Plese enter the number and range should be {startIndex} to {endIndex}")
        self.__skills_and_hobbiles_validation(
            message, startIndex, endIndex, skillsAndHobiles)

    def __addMarks(self, message) -> int:
        while True:
            marks = input(f"add {message} marks : ")
            if marks.isdigit() and 0 <= int(marks) <= 100:
                return int(marks)
            else:
                print("Please enter the marks in numbers and range is 0 to 100")

    def __str__(self):
        return (f"Student(id={self._student_id}, "
                f"name='{self._student_name}', "
                f"marks={self._student_marks}, "
                f"skills={self._student_skills}, "
                f"hobbies={self._student_hobbies})")
