from Ex6_1_Toy import Toy
from Ex6_1_Ball import Ball
from Ex6_1_Store import Store

print('---------------Toy---------------')
t1 = Toy(30, 'Red')
t1.print_data()

print('---------------Ball---------------')
b1 = Ball(30, 'Blue', 2.5, 'Rubber')
b1.print_data()

print('---------------Store---------------')
s1 = Store()
s1.add_toy(t1)
s1.add_toy(b1)
s1.play_all_toys()

