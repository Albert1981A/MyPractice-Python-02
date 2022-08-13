from Ex5_1_Student import Student

class School:
    def __init__(self):
        self.students = []
    
    # Receive a Student and add him to the collection of Students
    def add_student(self, student):
        arr = list(filter( lambda x : x.id == student.id ,self.students))
        if len(arr) > 0:
            print('Student already Exist')
        else:
            self.students.append(student)

    # Print the Data of all the Students in the school
    def print_students_data(self):
        for student in self.students:
            student.print_data()

s1 = Student(1, 'Avi', 2)
s1.add_grade(80)
s1.add_grade(60)
s1.add_grade(90)
s2 = Student(2, 'Ron', 3)
s2.add_grade(100)
s2.add_grade(70)
s2.add_grade(80)

sc = School()
sc.add_student(s1)
sc.add_student(s2)
sc.add_student(s1)

sc.print_students_data()
