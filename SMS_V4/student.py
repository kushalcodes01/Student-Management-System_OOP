class Student:

    def __init__(self, student_id, name, semester):
        self.student_id = student_id
        self.name = name
        self.semester = semester

    def __str__(self):
        return f"{self.student_id} | {self.name} | Semester: {self.semester}"