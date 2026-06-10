# chapter 9
print("\nchap 9")
# basic class
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()
your_dog.sit()

#car class
class Car():
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # return full name
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    # read miles
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading)
              + " miles on it.")
    # renew miles
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    # add miles
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# create obj
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # use parents class
        super().__init__(make, model, year)

        # subclass's own attributes
        self.battery_size = 70

    # subclass's own methods
    def describe_battery(self):

        print("This car has a "
              + str(self.battery_size)
              + "-kWh battery.")

    # override parents class
    def fill_gas_tank(self):

        print("This car doesn't need a gas tank!")


# create electriccar obj
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()


# 4. Battery calss(Composition)
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a "
              + str(self.battery_size)
              + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "
        message += str(range)
        message += " miles on a full charge."
        print(message)
    #practice
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

# 5. ElectricCar + Battery
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Composition: electric car "has" a battery obj
        self.battery = Battery()

# create obj
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# upgrade battery
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 6. Restaurant practice
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # default
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant name: "
              + self.restaurant_name.title())
        print("Cuisine type: "
              + self.cuisine_type.title())
    def open_restaurant(self):
        print(self.restaurant_name.title()
              + " is now open!")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant('kfc', 'fried chicken')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("People served:",
      restaurant.number_served)
restaurant.set_number_served(50)
print("People served:",
      restaurant.number_served)
restaurant.increment_number_served(20)
print("People served:",
      restaurant.number_served)

# 7. IceCreamStand(inherit)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    def show_flavors(self):
        print("Ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor.title())

ice_cream = IceCreamStand('sweet house', 'ice cream')
ice_cream.show_flavors()

# 8. User class
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("First name: "
              + self.first_name.title())
        print("Last name: "
              + self.last_name.title())
    def greet_user(self):
        print("Hello, "
              + self.first_name.title() + "!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('yunzhe', 'jiang')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts:",
      user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts:",
      user1.login_attempts)

# 9. Privileges class
class Privileges():
    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

# 10. Admin class(inherit + Composition)
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
admin = Admin('admin', 'root')
admin.describe_user()
admin.privileges.show_privileges()

# 11. OrderedDict (standard class)
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title()
          + "'s favorite language is "
          + language.title() + ".")

# 12. random / practice of dice
from random import randint
class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_dice(self):
        x = randint(1, self.sides)
        print(x)
# 6 sides dice
dice = Dice()
print("6-sided dice:")
for i in range(10):
    dice.roll_dice()
# 10 sides dice
dice10 = Dice(10)
print("10-sided dice:")
for i in range(10):
    dice10.roll_dice()
# 20 sides dice
dice20 = Dice(20)
print("20-sided dice:")
for i in range(10):
    dice20.roll_dice()