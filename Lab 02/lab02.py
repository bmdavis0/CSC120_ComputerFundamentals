# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Name: Ben Davis                                                 #
# File: lab02.py                                                  #
# Bb Name: bmdavis3                                               #
# This simple program gets 2 ints from user, adds them, then      #
# prints the sum.                                                 #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def add_two_nums():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    answer = num1 + num2
    print(f"The sum of {num1} and {num2} is: {answer}")


add_two_nums()
