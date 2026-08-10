import json
from student import Student

class StudentManagementSystem:
    def load_students(self):

        try:

            file = open("students.json", "r")

            data = json.load(file)

            for item in data:

                   student = Student(
                        item["student_id"],
                        item["name"],
                        item["semester"]
                   )

                   self.students.append(student)
            file.close()
        except FileNotFoundError:
             pass
            
    def __init__(self):
        self.students = []
        self.load_students()
    
    def save_students(self):

        data = []

        for student in self.students:
              data.append(student.to_dict())

        file = open("students.json", "w")

        json.dump(data, file, indent=4)

        file.close()
        
    def add_student(self):
    
        student_id = input("Enter the Id:")
    
        for student in self.students:
                if student.student_id == student_id:
                    print("This id already exist")
                    return
    
        name = input("Enter name of the student:").strip()
    
        if name == "":
                print("Name can't be empty")
                return
            
        try:
                semester = int(input("Enter Semester:"))
    
                if semester < 1 or semester > 8:
                    print("Semester must be between 1 and 8")
                    return
    
        except ValueError:
                print("Semester must be a number")
                return
            
    
        student = Student(student_id, name, semester)
    
        self.students.append(student)
        self.save_students()
        print("student Added Successfully")
    
    def view_student(self):
    
        if len(self.students) == 0:
            print("No Student Found")
            return
    
        for student in self.students:
            print(student)
            print("-----------")
    
    def search_student(self):
    
        search_id = input("Enter Id to Search:")
    
        found = False
    
        for student in self.students:
    
            if student.student_id == search_id:
                print(student)
                found = True
                break
    
        if not found:
            print("Not Found")
    
    def delete_student(self):
    
        delete_id = input("Enter id to delete:")
    
        found = False
    
        for student in self.students:
    
            if student.student_id == delete_id:
                self.students.remove(student)
                self.save_students()
                found = True
                break
    
        if not found:
            print("student Not found")
        else:
            print("Deleted Successfully")
    
    def update_student(self):
    
        update_id = input("Enter id to update:")
        found = False
    
        for student in self.students:
    
            if student.student_id == update_id:
    
                new_name = input("Enter new name:")
                if new_name.strip() == "":
                    print("Name cannot be empty")
                    return
                
                try:
                        new_semester = int(input("Enter new semester:"))
    
                        if new_semester < 1 or new_semester > 8:
                            print("Semester must be between 1 and 8")
                            return
    
                except ValueError:
                        print("Semester must be a number")
                        return
                    
                student.name = new_name    
                student.semester = new_semester
                self.save_students()
    
                found = True
                break
    
        if not found:
            print("Invalid ID")
    
        else:
                print("Student updated successfully")
    
    def search_by_name(self):
    
        search_name = input("Enter Namee:").strip()
    
        if search_name == "":
                print("Name cannot be empty")
                return
            
    
        found = False
    
        for student in self.students:
    
                if search_name.lower() in student.name.lower():
                    print(student)
                    found = True
    
        if not found:
                print("Not Found")
    
    def count_students(self):
            print("Total Students =", len(self.students))
    
    def statistics(self):
    
        semester_count = {}
    
        for student in self.students:
    
                sem = student.semester
    
                if sem in semester_count:
                    semester_count[sem] += 1
    
                else:
                    semester_count[sem] = 1
    
        for sem, count in semester_count.items():
                print("Semester:", sem, ":", count)
    