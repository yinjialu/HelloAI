cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
        
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print(1 == '1')
print(1 == 1)
print(1 > 0)
print(1 != 1)
print(1 < 3 and 1 > 0)
print(1 < 3 or 1 > 3)
print(1 in [1, 3])
print(1 not in [1, 3])

age = 18
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
    
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is 0.")
    
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 0 points!")
    
age = 65
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")  
    
    
fruits = ['apple', 'banana', 'orange', 'grape']
if 'apple' in fruits:
    print("You really like apple!")
if 'banana' in fruits:
    print("You really like banana!")
if 'orange' in fruits:
    print("You really like orange!")
if 'grape' in fruits:
    print("You really like grape!")
if 'peach' in fruits:
    print("You really like peach!")
    
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
users = ['admin', 'jialu', 'jialu', 'jialu', 'jialu']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
     
users = []   
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
    
current_users = ['admin', 'abc', 'def', 'ghi', 'jkl']
new_users = ['abc', 'mno', 'pqr', 'stu', 'vwx']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to enter a new username.")
    else:
        print("The username is available.")
        
list = list(range(1, 10))
for num in list:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")