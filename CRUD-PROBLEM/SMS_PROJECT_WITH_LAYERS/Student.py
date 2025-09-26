class Student:
    def __init__(self, id, name, marks=None, skills=None, hobbies=None):
        self.id = id
        self.name = name
        self.marks = marks or list()
        self.skills = skills or set()
        self.hobbies = hobbies or set()

    def __str__(self):
        return (f"""Student(
                id={self.student_id}, 
                name={self.name},
                marks={self.marks}, 
                skills={self.skills}, 
                hobbies={self.hobbies}
            )""")
