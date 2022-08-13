from datetime import date

class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.birth_year = 0

    def print_data(self):
        print('ID', self.id)
        print('Name', self.name)
        print('Birth Year', self.birth_year)
        print('---------------------')

    def print_age(self):
        current_year = date.today().year
        print('Age:', current_year - self.birth_year)
        print('---------------------')

    def get_animal(self, num_of_legs):
        if num_of_legs == 0:
            return 'Fish'
        elif num_of_legs <= 2:
            return 'Monkey'
        elif num_of_legs <= 4 and num_of_legs > 2:
            return 'Dog'
        else:
            return 'No Animal'


p1 = Person()
p1.id = 1
p1.name = "Ron"
p1.birth_year = 1995

p1.print_data()
p1.print_age()
print(p1.get_animal(0))

p2 = Person()
p2.id = 2
p2.name = "Dana"
p2.birth_year = 2002

p2.print_data()
p2.print_age()
print(p2.get_animal(2))
