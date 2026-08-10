class Student:

    def __init__(self, student_id, name, semester):
        self.student_id = student_id
        self.name = name
        self.semester = semester

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.semester}"

    def to_dict(self):
        return{
            "student_id" : self.student_id,
            "name" : self.name,
            "semester" : self.semester
        }

s1 = Student("101", "Kushal", 5)

print(s1.to_dict())