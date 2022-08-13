

class Toy:
    def __init__(self, price, color):
        self.__price = price
        self.__color = color
    
    def print_data(self):
        print('Price:', self.__price)
        print('Color:', self.__color)
    
    def play(self):
        print('playing the toy')

    def buy(self):
        print('buying the toy')

