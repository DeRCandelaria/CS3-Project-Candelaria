class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

course = Course("Mathematics")

student1 = Student("Thomas", 10)
student2 = Student("Patrick", 8)

course.add_student(student1)
course.add_student(student2)

print("Course:", course.name)

for student in course.students:
    print("Student's Name:", student.name," Grade Level:", student.grade_level)