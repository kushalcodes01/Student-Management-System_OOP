import sqlite3
from student import Student

class StudentManagementSystem:

    def __init__(self):

        self.conn = sqlite3.connect("school.db")
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        student_id TEXT PRIMARY KEY,
        name TEXT,
        semester INTEGER)
        """)

        self.conn.commit()

    def add_student(self):

        student_id = input("Enter ID:")
        name = input("Enter name:")

        try:
            semester = int(input("Enter Semester:"))
        except ValueError:
            print("Semester must be a number")
            return

        try:

            self.cursor.execute(
                "INSERT INTO students VALUES(?,?,?)",
                (student_id, name, semester)
            )

            self.conn.commit()

            print("Student Added Successfully")

        except sqlite3.IntegrityError:
            print("Student ID Already Exists")

    def view_students(self):

        self.cursor.execute("SELECT * FROM students")

        data = self.cursor.fetchall()

        if len(data) == 0:
            print("no Student found")
            return

        for row in data:

            student = Student(
                row[0],
                row[1],
                row[2]
            )

            print(student)

    def search_student(self):

        search_id = input("Enter ID to search:")

        self.cursor.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (search_id,)
        )

        data = self.cursor.fetchone() #fetchone() is used when only one record shpuld exists

        if data:

            student =(
                data[0],
                data[1],
                data[2]
            )
            print(student)

        else:
            print("Student Not Found")

    def update_students(self):

        update_id = input("Enter ID to udate:")

        new_name = input("Enter new name:")

        try:
            new_semester = int(input("Enter new semester:"))
        except ValueError:
            print("Semester must be a number")
            return

        self.cursor.execute(
            """
        UPDATE students
        SET name = ?, semester = ?
        WHERE student_id = ?
        """,
        (new_name, new_semester, update_id  )
        )

        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("Student Update successfully")

        else:
            print("Student not found")

    def delete_student(self):

        delete_id = input("enter id to delete:")

        self.cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (delete_id,)
        )

        self.conn.commit()

        if self.cursor.rowcount > 0 :
            print("Successfully Deleted")

        else:
            print("Student Not founnd")

