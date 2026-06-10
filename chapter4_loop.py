# chapter 4
print("\nchap 4")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")

#practice
pizza = ['pepperoni', 'pineapple', 'cheese']
for p in pizza:
    print("I like " + p + " pizza.")
print("I really love pizza!")
pets = ['cat', 'dog', 'rabbit']
for pet in pets:
    print("A " + pet + " would make a great pet.")
print("Any of these animals would make a great pet!")
#4.3
for value in range(1, 5):
    print(value)
for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(0, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
squares = [value ** 2 for value in range(1, 11)]
print(squares)
#practice
for value in range(1, 21):
    print(value)
hundred = list(range(1, 101))
for value in hundred:
    print(value)
thousand = list(range(1, 1001))
print(min(thousand))
print(max(thousand))
print(sum(thousand))
odd_numbers = list(range(1, 20, 2))
for value in odd_numbers:
    print(value)
div_by_three = list(range(3, 31, 3))
for value in div_by_three:
    print(value)
cube_of_ten = list(range(1, 11))
for value in cube_of_ten:
    print(value ** 3)
list_of_cubes = [value ** 3 for value in range(1, 11)]
print(list_of_cubes)
#4.4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:5])
print(players[2:])
print(players[-3:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#4.4.3
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#practice
print("The first three items in the list are:")
print(players[:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are:")
print(players[-3:])
pizza = ['pepperoni', 'pineapple', 'cheese', 'olives', 'mushrooms']
friend_pizza = pizza[:]
print("My favorite pizzas are:")
print(pizza)
print("\nMy friend's favorite pizzas are:")
print(friend_pizza)
pizza.append('bbq chicken')
friend_pizza.append('margherita')
print("\nMy favorite pizzas are:")
print(pizza)
print("\nMy friend's favorite pizzas are:")
print(friend_pizza)
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)
friend_foods = my_foods[:]
for food in friend_foods:
    print(food)
#4.5
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
#practice
# practice 4-13
restaurant_food = ('steak', 'salad', 'soup', 'bread', 'dessert')
print("Original menu:")
for food in restaurant_food:
    print(food)
# restaurant_food[0] = 'pizza'
# This will cause an error because tuples cannot be modified.
restaurant_food = ('pizza', 'salad', 'soup', 'rice', 'dessert')
print("\nNew menu:")
for food in restaurant_food:
    print(food)
