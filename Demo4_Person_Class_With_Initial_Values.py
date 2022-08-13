from datetime import date

class Person:
    def __init__(self, id, name, birth_year):
        self.id = id
        self.name = name
        self.birth_year = birth_year
    
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


p1 = Person(1, 'Avi', 1998)
p1.print_data()
p1.print_age()
print(p1.get_animal(3))

p2 = Person(2, 'Eva', 1982)
p2.print_data()
p2.print_age()
print(p2.get_animal(5))



