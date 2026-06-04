# chapter 6
print("\nchap 6")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

#practice
person = {
    'first_name': 'ada',
    'last_name': 'lovelace',
    'age': 28,
    'city': 'london',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#practice
favorite_numbers = {
    'alice': 7,
    'bob': 14,
    'cecilia': 21,
    'david': 3,
    'eric': 9,
}

print("Alice's favorite number is " + str(favorite_numbers['alice']) + ".")
print("Bob's favorite number is " + str(favorite_numbers['bob']) + ".")
print("Cecilia's favorite number is " + str(favorite_numbers['cecilia']) + ".")
print("David's favorite number is " + str(favorite_numbers['david']) + ".")
print("Eric's favorite number is " + str(favorite_numbers['eric']) + ".")

#practice
glossary = {
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'tuple': 'A list that cannot be changed.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A way to repeat actions.',
}

print("\nString:\n" + glossary['string'])
print("\nList:\n" + glossary['list'])
print("\nTuple:\n" + glossary['tuple'])
print("\nDictionary:\n" + glossary['dictionary'])
print("\nLoop:\n" + glossary['loop'])

#6.3loop through dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("\nThe following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

print("\nNo duplicate languages:")

for language in set(favorite_languages.values()):
    print(language.title())

#practice
glossary = {
    'string': 'A series of characters.',
    'list': 'Stores multiple items.',
    'tuple': 'Cannot be changed.',
    'dictionary': 'Stores key-value pairs.',
    'loop': 'Repeats actions.',
    'if': 'Makes decisions.',
    'float': 'Decimal number.',
    'boolean': 'True or False.',
    'variable': 'Stores data.',
    'function': 'Reusable block of code.',
}

for word, meaning in glossary.items():
    print("\n" + word.title())
    print(meaning)

#practice
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print("The " + river.title() +
          " runs through " +
          country.title() + ".")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())

#practice
people = ['jen', 'sarah', 'edward', 'phil', 'eric']

for person in people:
    if person in favorite_languages.keys():
        print(person.title() + ", thank you for taking the poll.")
    else:
        print(person.title() + ", please take the poll.")

#6.4nested
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#create 30 aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

#pizza example
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("\nYou ordered a " + pizza['crust'] + "-crust pizza with:")

for topping in pizza['toppings']:
    print(topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

    for language in languages:
        print(language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():

    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("Full name: " + full_name.title())
    print("Location: " + location.title())

#practice
people = []

person1 = {
    'first_name': 'alice',
    'last_name': 'smith',
    'age': 20,
    'city': 'new york',
}

person2 = {
    'first_name': 'bob',
    'last_name': 'johnson',
    'age': 25,
    'city': 'london',
}

person3 = {
    'first_name': 'cathy',
    'last_name': 'lee',
    'age': 22,
    'city': 'tokyo',
}

people.append(person1)
people.append(person2)
people.append(person3)

for person in people:
    print(person)

#practice
pets = []
pet1 = {
    'animal': 'dog',
    'owner': 'alice',
}
pet2 = {
    'animal': 'cat',
    'owner': 'bob',
}
pet3 = {
    'animal': 'rabbit',
    'owner': 'cathy',
}
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    print(pet)

#practice
favorite_places = {
    'alice': ['tokyo', 'paris', 'london'],
    'bob': ['beijing', 'new york'],
    'cathy': ['seoul'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places:")

    for place in places:
        print(place.title())

#practice
favorite_numbers = {
    'alice': [3, 7],
    'bob': [8, 10],
    'cathy': [1, 5],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers:")

    for number in numbers:
        print(number)

#practice
cities = {
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'Famous for sushi',
    },

    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'Has the Eiffel Tower',
    },

    'new york': {
        'country': 'usa',
        'population': '8 million',
        'fact': 'Called the Big Apple',
    },
}

for city, info in cities.items():
    print("\nCity: " + city.title())
    print("Country: " + info['country'].title())
    print("Population: " + info['population'])
    print("Fact: " + info['fact'])