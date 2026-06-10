# chapter 5
print("\nchap 5")
# 5.1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')
print("\nIs 5 > 3? I predict True.")
print(5 > 3)
print("\nIs 2 > 10? I predict False.")
print(2 > 10)
print("\nIs 7 <= 7? I predict True.")
print(7 <= 7)
print("\nIs 9 < 1? I predict False.")
print(9 < 1)
print("\nIs 'apple' == 'apple'? I predict True.")
print('apple' == 'apple')
print("\nIs 'cat' == 'dog'? I predict False.")
print('cat' == 'dog')

# 5.2 More Conditional Tests
food = 'Pizza'
print(food.lower() == 'pizza')
print(food.lower() == 'burger')
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 9)
age = 20
print(age > 18 and age < 30)
print(age < 18 or age > 15)
fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)
print('grape' in fruits)
print('grape' not in fruits)
print('banana' not in fruits)

# 5.3 Simple if statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# if-else
print("\nif-else example")
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
# if-elif-else
print("\nif-elif-else example")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
# Multiple elif
print("\nMultiple elif example")
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# Multiple if statements
print("\nMultiple if statements")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# 5-3 Alien Colors #1
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

# 5-4 Alien Colors #2
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

# 5-5 Alien Colors #3
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

# 5-6 Stages of Life
age = 25
if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

# 5-7 Favorite Fruit
print("\n5-7 Favorite Fruit")
favorite_fruits = ['banana', 'apple', 'watermelon']
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'watermelon' in favorite_fruits:
    print("You really like watermelons!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")

# 5.4 Working with Lists and if Statements
print("\n5.4 Working with Lists and if Statements")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# Checking special items
print("\nChecking special items")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# Empty list
print("\nEmpty list example")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
# Multiple lists
print("\nMultiple lists example")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

# 5-8 Hello Admin
usernames = ['admin', 'eric', 'john', 'alice', 'david']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")

# 5-9 No Users
usernames = []
if usernames:
    for username in usernames:
        print("Hello " + username)
else:
    print("We need to find some users!")

# 5-10 Checking Usernames
current_users = ['alice', 'bob', 'charlie', 'david', 'eric']
new_users = ['Bob', 'kevin', 'david', 'lucy', 'ALICE']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + " will need to enter a new username.")
    else:
        print(new_user + " is available.")