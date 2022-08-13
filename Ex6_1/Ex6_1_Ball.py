
from Ex6_1_Toy import Toy

class Ball(Toy):
    def __init__(self, price, color, radius, material):
        super().__init__(price, color)
        self.__radius = radius
        self.__material = material
    
    def print_data(self):
        super().print_data()
        print('Radius:', self.__radius)
        print('Material:', self.__material)
    
    def play(self):
        print('playing the Ball')

    def buy(self):
        print('buying the Ball')

