from Ex6_2_Animal import Animal

class Monkey(Animal):
    def __init__(self, num_of_legs, color):
        super().__init__(num_of_legs)
        self.__color = color

    def print_data(self):
        print("Num of Legs:", self._Animal__num_of_legs)
        print("Color:", self.__color)

    def eat(self):
        print('Monkey is eating')

# m1 = Monkey(2, 'Black')
# m1.print_data()
# m1.eat()