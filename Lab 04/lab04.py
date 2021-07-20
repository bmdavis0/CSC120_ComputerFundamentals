# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Name: Ben Davis                                                 #
# File: lab04.py                                                  #
# Bb Name: bmdavis3                                               #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Question 1: Write a for loop that prints all numbers from 10 to 99.
print("QUESTION 1")

for i in range(10, 100):
    print(i)
print()

# Question 2: Write a program to input a number from the user.  Determine if the number is a single or double digit.
print("QUESTION 2")
num = int(input("Please enter a number between 0 and 99: "))

if num < 10:
    print(f"{num} is a single digit number.")
elif num >= 10:
    print(f"{num} is a double digit number.")
print()

# Question 3: Write a for loop that prints all even numbers from 10 to 99 (10 inclusive)
print("QUESTION 3")
print("Option 1")

for num in range(10, 100):
    if num % 2 == 0:
        print(num)
print()

# Now, if you specifically wanted it to append to a list...
print("QUESTION 3")
print("Option 2")
even_list = []

for num in range(10, 100):
    if num % 2 == 0:
        even_list.append(num)
print(even_list)
print()

# Question 4: Write a for loop that prints the table of 5 shown in prompt.
print("QUESTION 4")
table_list = []

for num in range(5, 51, 5):
    table_list.append(num)
    print(num)
print()

# Question 5: Write a for loop that prints all the numbers in the table of 5 that are divisible by 3.
print("QUESTION 5")

for i in table_list:
    if i % 3 == 0:
        print(f"{i} is divisible by 3.")
    else:
        print(i)
print()

# Question 6A: How would you fix the following error?
print("QUESTION 6A")
print("To fix the error, include a  colon(:) symbol after the first line.")
print("for i in range(20):")
print()

# Question 6B: How would you fix the following error?
print("QUESTION 6B")
print("To fix the error, indent the second line.")
print("for i in range(20):")
print("    print(i)")
print()

# Question 7: You are provided a list.  Print the elements to the console.
print("QUESTION 7")
prices = [10, 130, 25, 64, 91, 66, 42, 18, 141, 64]

for i in prices:
    print(i)
print()

# Question 8: Using the list from the previous question, filter all the elements that are above 20 and less than 80.
# Add them to a new list.  This list should be called FILTERED_LIST
print("QUESTION 8")
filtered_list = []

for i in prices:
    if 20 < i < 80:
        filtered_list.append(i)
print("I'm assuming you want the new list printed.  Directions didn't ask explicitly for that, but...")
print(filtered_list)
print()

# Question 9: Write a program that accepts a username and a password from the user.  If the username entered
# is "student007" and password entered is "new_password", your program should print "Login successful."
# Else, print "Try again.  Login failure."
print("QUESTION 9")
user = input("Enter username: ")
password = input("Enter password: ")

if user == "student007" and password == "new_password":
    print("Login successful.")
else:
    print("Try again. Login failure.")
print()

# Question 10: Write a program to accept a username from a user.  If the length of the username is less than 5
# characters, or if the length is greater than 16 characters, print "Invalid username." Else, print "Valid username."
print("QUESTION 10")
user2 = input("Enter username: ")

if len(user2) < 5 or len(user2) > 16:
    print("Invalid username.")
else:
    print("Valid username.")
print()

# Challenge Question 1: You have a list of prices in a store.  Write a program that prints all pairs of items
# that add up to 50.
print("CHALLENGE QUESTION 1")
item_prices = [10, 40, 1, 16, 25, 34, 49, 40]

# for i in item_prices:
#     for j in item_prices:
#         if i + j == 50:
#             print(f"{i}, {j}")

for i in range(len(item_prices)):
    for j in range(len(item_prices)):
        if i < j:
            if item_prices[i] + item_prices[j] == 50:
                print(f"{item_prices[i]}, {item_prices[j]}")
print()

# Challenge Question 2: Ask a user for a name, and compare input against provided list.  If name is found, print
# "name found: <name>".  Else, print name not found.
print("CHALLENGE QUESTION 2")
names = ["sarang", "john", "lily", "jasmine", "mara", "dave", "chester"]
name_input = input("Enter a name to search for: ").lower()

output = "Name not found."

for i in names:
    if name_input == i:
        output = f"Name found: {name_input}"

print(output)
