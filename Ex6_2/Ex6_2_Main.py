from ast import Import
from Ex6_2_Animal import Animal
from Ex6_2_Zebra import Zebra
from Ex6_2_Monkey import Monkey
from Ex6_2_Chimpanzee import Chimpanzee
from Ex6_2_Zoo import Zoo

print('---------------Animal---------------')
a1 = Animal(2)
a1.eat()

print('---------------Zebra----------------')
z1 = Zebra(4, 100)
z1.print_data()
z1.eat()

print('---------------Monkey---------------')
m1 = Monkey(4, 'Black')
m1.print_data()
m1.eat()

print('-------------Chimpanzee-------------')
c1 = Chimpanzee(3, "brown", 1.5)
c1.print_data()
c1.eat()

print('-----------------Zoo----------------')
zoo = Zoo()
zoo.add_animal(a1)
zoo.add_animal(z1)
zoo.add_animal(m1)
zoo.add_animal(c1)
print("Number of Animals: " + str(zoo.count_animals()))
zoo.feed_the_animals()