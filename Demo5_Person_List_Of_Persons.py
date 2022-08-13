from datetime import date

class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.birth_year = 0
        self.phones = []

    def print_data(self):
        print('ID', self.id)
        print('Name', self.name)
        print('Birth Year', self.birth_year)
        print('Phones:', self.phones)
        print('---------------------')

    def print_age(self):
        current_year = date.today().year
        print('Age:', current_year - self.birth_year)
        print('---------------------')

p1 = Person()
p1.id = 1
p1.name = "Ron"
p1.birth_year = 1995
p1.phones.append("052-5566888")
p1.phones.append("053-5577999")

p2 = Person()
p2.id = 2
p2.name = "Dana"
p2.birth_year = 2002
p2.phones.append("057-5522444")

arr = [p1, p2]

for p in arr:
    p.print_data()
    p.print_age()
