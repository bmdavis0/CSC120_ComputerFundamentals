# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Name: Ben Davis                                                 #
# File: lab03.py                                                  #
# Bb Name: bmdavis3                                               #
# This program gets a number from the user and prints whether the #
# number is odd, even, or negative. It then prints the first 20   #
# even numbers sequentially.                                      #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def main():
    get_num()
    print()
    even_numbers()


def get_num():
    user_num = int(input("Please enter a number: "))
    if user_num < 0:  # checking for negative numbers
        if user_num % 2 == 0:
            print(f"{user_num} is a negative even number.")
        else:
            print(f"{user_num} is a negative odd number.")
    elif (user_num % 2) == 0:  # checks if number is even
        print(f"{user_num} is an even number.")
    else:
        print(f"{user_num} is an odd number.")


def even_numbers():
    count = 0
    num = 0
    while count < 20:
        if num % 2 == 0:  # checks for even number
            print(num)
            count += 1
            num += 2


main()
