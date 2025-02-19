from random import randint, choice
# print(randint(1, 6))

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
    
default_die = Die()
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())
# print(default_die.roll_die())

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lucky_numbers = []
for i in range(4):
    lucky_numbers.append(choice(lottery_list))
print(lucky_numbers)
print("if you have this number, you win the lottery!")

my_ticket = []
time = 0
while my_ticket != lucky_numbers:
    time += 1
    lucky_numbers = []
    for i in range(4):
        lucky_numbers.append(choice(lottery_list))
    print(lucky_numbers)
print(time)


