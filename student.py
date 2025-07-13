class Student:
    def __init__(self, roll, name, course, marks):
        self.roll = roll
        self.name = name
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll}, Name: {self.name}, Course: {self.course}, Marks: {self.marks}"
