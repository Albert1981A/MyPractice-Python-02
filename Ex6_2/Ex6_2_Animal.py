
class Animal:
    def __init__(self, num_of_legs):
        self.__num_of_legs = num_of_legs
    
    def eat(self):
        print('Animal is eating')

# a1 = Animal(2)
# a1.print_data()
# a1.eat()