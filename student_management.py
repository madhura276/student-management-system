import student as s
import os

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, roll, name, course, marks):
        student = s.Student(roll, name, course, marks)
        self.students.append(student)

    def view_students(self):
        for student in self.students:
            print(student)

    def search_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                return student
        return None

    def update_marks(self, roll, new_marks):
        student = self.search_student(roll)
        if student:
            student.marks = new_marks
            print("✅ Marks updated.")
        else:
            print("❌ Student not found.")

    def calculate_average(self):
        if not self.students:
            return 0
        total = sum([student.marks for student in self.students])
        return total / len(self.students)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for student in self.students:
                file.write(f"{student.roll},{student.name},{student.course},{student.marks}\n")

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print("📂 No saved file found.")
            return
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4:
                    roll, name, course, marks = data
                    self.add_student(int(roll), name, course, int(marks))
