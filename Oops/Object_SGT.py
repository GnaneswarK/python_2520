from StudentGradeTracker import StudentGradeTracker

while True:
    student_id = input("Enter Student ID : ")
    if student_id.isdigit():
        student_id = int(student_id)
        break
    else:
        print("Enter valid ID")
student_name = input("Enter Student Name : ")
while True:
    attendance = input("Enter Student Attendance : ")
    if attendance.isdigit():
        attendance = int(attendance)
        break
    else:
        print("Enter Valid Attendance")

sgt: StudentGradeTracker = StudentGradeTracker(
    student_id, student_name, attendance)

sgt.add_score()

#   FOR PRINTING ID NAME ATTENDACE
print(sgt)

print(f"TOTAL Score : {sgt.total_score()}")

print("At least one score should be available to find average" if sgt.avg_score(
) == -1.0 else f"AVERAGE MARKS : {sgt.avg_score()}")

print(f"Count of the Scores : {sgt.number_of_scores()}")

print(f"Grade of an Student : {sgt.grade()}")

print(f"Attendace Criterial : {sgt.attendance_criteria()}")

sgt.award_eligibility()
