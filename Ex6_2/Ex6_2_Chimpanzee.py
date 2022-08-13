from Ex6_2_Monkey import Monkey

class Chimpanzee(Monkey):
    def __init__(self, num_of_legs, color, height):
        super().__init__(num_of_legs, color)
        self.__height = height

    def print_data(self):
        super().print_data()
        print("Height:", self.__height)

    # We don't need to write the eat() function 
    # This is because we receives it from the super ("Monkey")
    
c1 = Chimpanzee(3, "brown", 1.5)
c1.print_data()
c1.eat()
