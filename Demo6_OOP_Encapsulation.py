# Encapsulation 

class Person:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.__phones = [] # writing "phones" with two underlines ( like this: "__phones" ) will make it "private"
        # one under line is "protected" ( like this: "_phones" )

    def add_phone(self, phone):
        if len(phone) == 9:
            self.__phones.append(phone)
        else: 
            print('phone is invalid')
    
    def print_data(self):
        print('id:', self.id)
        print('Name:', self.name)
        print('phones:', self.__phones)

p1 = Person()
p1.id = 1
p1.name = 2 
p1.add_phone("052-66666") # We can access the "__phone" only by the function 
p1.print_data()
p1.__phones.append('052-55555') # We cannot access the "__phone" directly because its private


# 02:19:42