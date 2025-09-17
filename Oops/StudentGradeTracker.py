import math


class StudentGradeTracker:
    def __init__(self, id: int, name: str, attendance: int) -> None:
        self.id = id
        self.name = name
        self.attendance = attendance
        self.score = []

    def add_score(self) -> None:
        condition_check = input(
            "Do you want to enter another score ? (yes/no) ")
        if condition_check.lower() == "yes":
            while True:
                value = input("Enter the score : ")
                if not value.isdigit():
                    print("Enter numeric value ")
                else:
                    self.__score(int(value))
                    break
            self.add_score()
        elif (condition_check.lower() != "no"):
            print("Please enter Either yes or no")
            self.add_score()

    def __score(self, value: int) -> None:
        self.score.append(value)

    def total_score(self) -> int:
        return sum(self.score)

    def number_of_scores(self) -> int:
        return len(self.score)

    def avg_score(self) -> float:
        if self.score:
            return self.total_score()/self.number_of_scores()
        else:
            return -1

    def grade(self) -> str:
        average_marks = math.floor(self.avg_score())
        grade_result = ""
        if average_marks < 50:
            grade_result = "Fail"
        elif average_marks < 70:
            grade_result = "C"
        elif average_marks < 85:
            grade_result = "B"
        else:
            grade_result = "A"
        return grade_result

    def attendance_criteria(self) -> str:
        if self.attendance < 75:
            return "WARNING LOW ATTENDANCE"
        else:
            return "GOOD ATTENDANCE"

    def award_eligibility(self) -> None:
        att_ctr: str = self.attendance_criteria()
        gdr: str = self.grade()

        if att_ctr == "GOOD ATTENDANCE" and gdr == "A":
            print("Eligible for award")
        else:
            print("Not eligible for award")

    def __str__(self) -> str:
        return f"Student ID : {self.id}\nStudent Name : {self.name}\nStudent Attendance : {self.attendance}"
