

class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)
    
    def count_animals(self):
        return len(self.__animals)
    
    def feed_the_animals(self):
        for animal in self.__animals:
            animal.eat()

