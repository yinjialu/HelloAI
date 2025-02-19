class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.name_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
        
    def get_name_served(self):
        print(f"{self.name_served} people have been served.")
        
    def set_name_served(self, served):
        self.name_served = served
    
    def increment_name_served(self):
        served  = int(input("How many people have been served? "))
        self.name_served += served
        
restaurant = Restaurant('The Mean Queen', 'pizza')
print(f"My favorite restaurant is {restaurant.restaurant_name}.")
restaurant = Restaurant('Taco Bell', 'tacos')
restaurant.describe_restaurant()
restaurant.open_restaurant()
# restaurant.increment_name_served()
restaurant.get_name_served()

restaurant = Restaurant('Subway', 'sandwiches') 
restaurant.describe_restaurant()

class User:
    def __init__(self, first_name, last):
        self.first_name = first_name
        self.last = last
        self.login_attempts = 0
    
    def get_login_attempts(self):
        print(f"{self.login_attempts} login attempts have been made.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name} {self.last} is a user.")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last}!")
        
user = User('John', 'Doe')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(24)
my_new_car.read_odometer()
my_new_car.update_odometer(22)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_su7 = ElectricCar('tesla', 'model s', 2019)
print(my_su7.get_descriptive_name())

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    def display_flavors(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("The privileges are:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
class Admin(User):
    def __init__(self, first_name, last):
        super().__init__(first_name, last)
        self.privileges = Privileges()
        
admin = Admin('John', 'Doe')
admin.privileges.show_privileges()