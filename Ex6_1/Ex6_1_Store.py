

class Store:
    def __init__(self):
        self.__toys = []

    def add_toy(self,toy):
        self.__toys.append(toy)

    def play_all_toys(self):
        for toy in self.__toys:
            toy.play()
