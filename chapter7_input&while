# chapter 7
print("\nchap 7")
# input() basics
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# clear input prompt
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# multi-line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")


# numeric input with int()
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are too young to vote.")


# roller coaster example
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")


# modulo operator %
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")


# basic while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# user chooses when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
#prompt = prompt + "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


# using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# using break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# using continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# avoiding an infinite loop
x = 1
while x <= 5:
    print(x)
    x += 1

# moving items between lists
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# removing all instances of a value
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n-Poll Results-")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# pizza toppings exercise
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' to finish. "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print("Adding " + topping + " to your pizza.")

# movie ticket exercise
while True:
    age = input("\nEnter your age (or 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

# deli exercise
sandwich_orders = ['tuna', 'ham', 'veggie']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# pastrami sold out exercise
sandwich_orders = [
    'pastrami',
    'tuna',
    'pastrami',
    'veggie',
    'pastrami',
    'ham'
]
finished_sandwiches = []
print("Sorry, we are out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# dream vacation poll
responses = {}
active = True
while active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place
    repeat = input("Would you like another person to respond? (yes/no) ")
    if repeat == 'no':
        active = False
print("\n--- Dream Vacation Places ---")
for name, place in responses.items():
    print(name + " would like to visit " + place + ".")