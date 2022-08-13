

class Person:  # Base class
    def __init__(self):
        self.id = 0
        self.name = ''
    
    def print_data(self):
        print('ID:', self.id)
        print('Name:', self.name)


class Employee(Person):  # Derived class (inherit "Person")
    def __init__(self):
        super().__init__()  # We received "Person" attributes by "super"
        self.department = ''

    def print_data(self):
        super().print_data # We are calling the print_data from the super
        print('Department', self.department)



p1 = Person()
p1.id = 1
p1.name = 'Ron'
p1.print_data()

e1 = Employee()
e1.id = 2
e1.name = 'Dana'
e1.department = 'Cars'
e1.print_data() # If "Employee" don't have this function it will call the function of "Person"