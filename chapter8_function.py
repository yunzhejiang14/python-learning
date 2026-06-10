# chapter 8
print("\nchap 8")
# defining a simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

# passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')
greet_user('sarah')

# positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

# calling a function multiple times
describe_pet('dog', 'willie')

# order of positional arguments matters
describe_pet('harry', 'hamster')

# keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')

# equivalent function calls
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# avoiding argument errors
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# practice
def display_message():
    print("I am learning about functions in Python.")
display_message()

def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")
favorite_book('alice in wonderland')

def make_shirt(size, message):
    print("\nThe shirt size is " + size + ".")
    print("The message is: " + message)
make_shirt('M', 'I love Python')
make_shirt(size='L', message='Coding is fun')

def make_shirt(size='L', message='I love Python'):
    print("\nThe shirt size is " + size + ".")
    print("The message is: " + message)
make_shirt()
make_shirt(size='M')
make_shirt(size='S', message='Hello World')

def describe_city(city, country='Iceland'):
    print(city.title() + " is in " + country.title() + ".")
describe_city('reykjavik')
describe_city('akureyri')
describe_city('beijing', 'china')

# returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# optional arguments
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted full name."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
# returning a dictionary with optional information
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# combining functions and while loops
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def city_country(city, country):
    return city.title() + ", " + country.title()
print(city_country('santiago', 'chile'))
print(city_country('beijing', 'china'))
print(city_country('berlin', 'germany'))

def make_album(artist, title, songs=''):
    """Return a dictionary containing album information."""
    album = {
        'artist': artist,
        'title': title
    }
    if songs:
        album['songs'] = songs
    return album

album1 = make_album('jay chou', 'fantasy')
album2 = make_album('adele', '25')
album3 = make_album('taylor swift', 'red', 16)
print(album1)
print(album2)
print(album3)

while True:
    print("\nEnter album information.")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)

# passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"

        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# printing models without functions
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# printing models with functions
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all printed models."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# preventing a function from modifying a list
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magician_names = ['alice', 'david copperfield', 'houdini']
show_magicians(magician_names)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("The Great " + magician.title())
    return great_magicians
great_magicians = make_great(magician_names)
show_magicians(great_magicians)
original_magicians = ['alice', 'david copperfield', 'houdini']
great_magicians = make_great(original_magicians[:])
print("\nOriginal list:")
show_magicians(original_magicians)
print("\nModified list:")
show_magicians(great_magicians)

# arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# positional argument with arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics'
)
print(user_profile)

def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print("- " + item)
make_sandwich('ham')
make_sandwich('ham', 'cheese')
make_sandwich('ham', 'cheese', 'tomato', 'lettuce')

my_profile = build_profile(
    'yunzhe',
    'jiang',
    location='berlin',
    major='ece',
    hobby='travel'
)
print(my_profile)

def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car
car = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True
)
print (car)


# saving functions in a module
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# importing an entire module
import chapter8_pizza

chapter8_pizza.make_pizza(16, 'pepperoni')
chapter8_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing a specific function
from chapter8_pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# using "as" to give a function an alias
from chapter8_pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# using "as" to give a module an alias
import chapter8_pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing all functions in a module
from chapter8_pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')