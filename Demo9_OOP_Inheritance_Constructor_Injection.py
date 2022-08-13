
# Constructor Injection

class Person:  # Base class
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def print_data(self):
        print('ID:', self.__id)
        print('Name:', self.__name)
        print('-----------------------')


class Employee(Person):  # Derived class (inherit "Person")
    def __init__(self, id, name, department):
        super().__init__(id, name)  # We received "Person" attributes by "super"
        self.__department = department

    def print_data(self):
        super().print_data() # We are calling the print_data from the super
        print('Department', self.__department)
        print('-----------------------')


p1 = Person(1, 'Ron')
p1.print_data()

e1 = Employee(2, 'Dana', 'Cars')
e1.print_data() # If "Employee" don't have this function it will call the function of "Person"



# 3:29:29