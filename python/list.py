bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])

friends = ['jialu', 'yue', 'yueyue', 'yueyueyue']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[-1].title())

print(f"Hello, {friends[0].title()}")
print(f"Hello, {friends[1].title()}")
print(f"Hello, {friends[2].title()}")
print(f"Hello, {friends[3].title()}")

ways = ['car', 'bus', 'bike', 'walk']
print(f"I would like to own a {ways[0].title()}")
print(f"I would like to own a {ways[1].title()}")
print(f"I would like to own a {ways[2].title()}")
print(f"I would like to own a {ways[3].title()}")

customers = ['jialu', 'yue', 'yueyue', 'yueyueyue']
print(customers)

remove_one = 'yue'

customers.remove(remove_one) # remove() removes an item by value
print(customers)

customers.append('yueyueyueyue') # append() always adds to the end of a list
print(customers)

customers.insert(0, 'yue') # insert() adds a new item at any position in the list
print(customers)

del customers[-1] # del statement removes an item by index
print(customers)

customers.pop() # pop() removes the last item in a list
print(customers)

customers.pop(0) # pop() can also remove an item by index
print(customers)

customers.append('yueyueyue')
print(customers)

print('只能邀请两位嘉宾共进晚餐')

remove_customer = customers.pop()
print(f"抱歉，{remove_customer}，无法邀请您共进晚餐")

print(f"总共邀请 {len(customers)} 位嘉宾共进晚餐")

invited_customer = customers.pop()
print(f"欢迎，{invited_customer}，邀请您共进晚餐")

invited_customer = customers.pop()
print(f"欢迎，{invited_customer}，邀请您共进晚餐")

print(customers)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort() changes the order of the list permanently
print(cars)

cars.sort(reverse=True) # sort(reverse=True) changes the order of the list permanently
print(cars)

print(sorted(cars)) # sorted() changes the order of the list temporarily
print(sorted(cars, reverse=True)) # sorted() changes the order of the list temporarily

print('cars', cars)
cars.reverse() # reverse() changes the order of the list permanently
print(cars) # reverse() changes the order of the list permanently

print(len(cars)) # len() returns the length of a list

travel = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'chengdu']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel, reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

print(travel[-1])

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you, everyone. That was a great magic show!")

pisa = ['pepperoni', 'mushroom', 'sausage', 'cheese']
for pizza in pisa:
    print(f"I like {pizza} pizza.")
    print(f"I really love pizza!\n")
    
    
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet.")
    print(f"Any of these animals would make a great pet!\n")
    
for value in range(1, 5):
    print(value)
    
print(range(1, 6))
print(list(range(1, 6)))

evens = list(range(2, 11, 2))
print(evens)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for value in range(1, 21):
    print(value)
    
# for value in range(1, 1000001):
#     print(value)
    
nums = [value for value in range(1, 1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))

for value in range(1, 21, 2):
    print(value)

for value in range(3, 31, 3):
    print(value)

for value in range(1, 11):
    print(value ** 3)
    
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])

for player in players[:2]:
    print(player.title())
    
print(f"The first three players on my team are: {players[:3]}")
print(f"The middle three players on my team are: {players[1:4]}")
print(f"The last three players on my team are: {players[-3:]}")

friend_pisa = pisa[:]
print(pisa)
friend_pisa.append('pepper')
print(friend_pisa)

dimensions = (200, 50)

foods = ('pizza', 'burger', 'hotdog', 'fries', 'salad')
for food in foods:
    print(food)
    
foods = ('pizza', 'burger', 'hotdog', 'fries', 'salad', 'cake')
for food in foods:
    print(food)