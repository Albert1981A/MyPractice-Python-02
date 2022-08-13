class Person:  # Base class
    def __init__(self):
        self.id = 0
        self.name = ''

class Employee(Person):  # Derived class (inherit "Person")
    def __init__(self):
        super.__init__()  # We received "Person" attributes by "super"
        self.department = ''

p1 = Person()
p1.id = 1
p1.name = 'Ron'

e1 = Employee()
e1.id = 2
e1.name = 'Dana'
e1.department = 'Cars'