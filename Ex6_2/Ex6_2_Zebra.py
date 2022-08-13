from Ex6_2_Animal import Animal

class Zebra(Animal):
    def __init__(self, num_of_legs, num_of_strips):
        super().__init__(num_of_legs)
        self.__num_of_strips = num_of_strips 

    def print_data(self):
        print("Num of Legs:", self._Animal__num_of_legs)
        print("Num of Strips:", self.__num_of_strips)

    def eat(self):
        print('Zebra is eating')

# z1 = Zebra(4, 100)
# z1.print_data()
# z1.eat()
