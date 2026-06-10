# Chapter 10: Files, Exceptions, JSON
print("\nchap 10")
# 1. Reading a file
# Open and read an entire file
filename = 'chapter10_pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())

# 2. Reading a file line by line
filename = 'chapter10_pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 3. Storing file lines in a list
filename = 'chapter10_pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 4. Building a long string from a file
filename = 'chapter10_pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 5. Writing to a file
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love Python.\n")

# 6. Appending to a file
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love data analysis.\n")
    file_object.write("I also love embedded systems.\n")


# 7. Basic exception handling
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# 8. Using try-except inside a loop
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    else:
        print(answer)

# 9. Handling FileNotFoundError
filename = 'chapter10_alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the file does not exist.")
else:
    print(contents[:100])

# 10. Counting words in a file
filename = 'chapter10_alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("File not found.")
else:
    # Split the text into words
    words = contents.split()
    # Count the words
    num_words = len(words)
    print("The file has about " + str(num_words) + " words.")

# 11. Using pass to fail silently
filename = 'missing_file.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
    print(contents)

# 12. Counting specific words
line = "Row, row, row your boat"
print(line.lower().count('row'))


# 13. Saving data with JSON
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

# 14. Loading data from JSON
import json
filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)

# 15. Remembering a user's name
import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
print("We will remember you when you come back, " + username + "!")

# 16. Reading the saved username
import json
filename = 'username.json'
with open(filename) as file_object:
    username = json.load(file_object)
print("Welcome back, " + username + "!")

# 17. Complete username remember program
import json
filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    print("We will remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# 18. Refactored version using functions
import json
def get_stored_username():
    """
    Get stored username if it exists.
    """
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """
    Ask for a new username and save it.
    """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username
def greet_user():
    """
    Greet the user.
    """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")
greet_user()