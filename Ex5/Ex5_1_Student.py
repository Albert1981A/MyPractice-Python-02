
class Student:
    def __init__(self, id, name, max_grades):
        self.id = id
        self.name = name
        self.grades = []
        self.max_grades = max_grades

    # Print the Students data (including his grades)
    def print_data(self):
        print('ID:', self.id)
        print('Name:', self.name)
        print('Grades:', self.grades)
        print('-------------------------')

    # Get a grade as parameter and add it to the grades array
    def add_grade(self, grade):
        if len(self.grades) >= self.max_grades:
            print('You cannot enter more than,', self.max_grades, 'grades !')
        else: 
            self.grades.append(grade)
            print('Grade added:', self.grades)
            print('-------------------------')

    # Will return the average of his grades
    def get_avg(self):
        return sum(self.grades) / len(self.grades)


s1 = Student(1, "Avi", 3)
s1.add_grade(80)
s1.add_grade(90)
s1.add_grade(70)
s1.add_grade(100)
s1.add_grade(80)

s1.print_data()

avg_s1 = s1.get_avg()
print(avg_s1)


# 49:20