# ---------------------- #
# Author: Ben Davis      #
# File name: midterm.py  #
# Class: CSC 120         #
# ---------------------- #

# PROGRAMMING QUESTIONS
# QUESTION 1
def most_significant_bit():
    test_string = input("Please enter a string of bits [0s + 1s]: ")
    print(f"The Most Significant Bit is: {test_string[0]}!")


most_significant_bit()
print()


# QUESTION 2
username = input("Please enter a new username: ")
if len(username) <= 6:
    print("Invalid username.  Please enter 6 or more characters.")
elif not username.islower():
    print("Invalid username.  Please use lowercase characters.")
else:
    print("Username accepted.")
print()


# QUESTION 3
i = 7
for j in range(1, 10):
    if j > i:
        print(j)
print()


# QUESTION 4
for i in range(0, 21):
    print(2 ** i)
