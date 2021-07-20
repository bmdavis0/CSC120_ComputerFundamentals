# ---------------------- #
# Author: Ben Davis      #
# File name: lab05.py    #
# Class: CSC 120         #
# ---------------------- #
import random

#  1 - Learn to Write Pseudocode - Find max value in a list
print("Lab Question #1")
list1 = [1, 23, 454, 543, 2, 123]
high_number = list1[0]

for x in list1:
    if x > high_number:
        high_number = x
print(high_number)
print()

#  2 - Convert the following code into the function create_list()
# import random
# MAX_LEN = 50
# my_list = []
# for i in range(MAX_LEN):
#     my_list.append(random.randint(1, 99))
print("Lab Question #2")


def create_list():
    MAX_LEN = 50
    my_list = []
    for num in range(MAX_LEN):
        my_list.append(random.randint(1, 99))
        print(my_list)
        return my_list


create_list()
print()

#  3 - Find the length of all the strings in the below list.  Use a for or a while loop
print("Lab Question #3")
names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]
count_list = []

for i in names:
    count_list.append(len(str(i)))
print(count_list)
print()

#  4 - Write a program to find the count of all names that are <= than itself in the provided list.
#      Use two nested loops to get all points.
print("Lab Question #4")
names2 = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]


def for_short_names():
    shorter = []

    for k in names2:
        for k2 in names2:
            if len(k) > len(k2):
                shorter.append(k2)

        length = len(shorter)
        print(f"The name {k} is longer than: {length}.")

        if len(shorter) > 0:
            print(shorter)
            shorter = []
        print()


for_short_names()


#  5 - Modify the above program to use two nested while loops
print("Lab Question #5")
names3 = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]


def while_short_names():
    shorter2 = []
    count = 0
    idx1 = 0

    while idx1 < len(names3):
        idx2 = 0
        while idx2 < len(names3):
            if len(names3[idx1]) >= len(names3[idx2]):
                if names3[idx1] != names3[idx2]:
                    count += 1
                    shorter2.append(names3[idx2])
                    idx2 += 1
                else:
                    idx2 += 1
            else:
                idx2 += 1
        print(f"Names shorter than or equal to {names3[idx1]} are {count} names.")
        print(shorter2)
        print()
        idx1 += 1
        shorter2 = []
        count = 0


while_short_names()


#   6 - Implement a leaderboard using a list.  The leaderboard tracks the top 5 scores that have been posted.
#       If a higher score has been achieved, the leaderboard refreshes with the new top 5 scores.
print("Lab Question #6")


def leaderboard():
    top_scores = []

    for i in range(50):
        rand_num = random.randint(0, 100)
        if len(top_scores) < 5:
            top_scores.append(rand_num)
            top_scores.sort()
            print(top_scores)

        elif rand_num > min(top_scores):
            top_scores.remove(min(top_scores))
            top_scores.append(rand_num)
            top_scores.sort()
            print(top_scores)

    print(top_scores)


leaderboard()
print()

print("Lab Question #6 - Optional Refactor")
hi_scores = [99, 87, 89, 99, 65]


def leaderboard2(new_score):
    for v in hi_scores:
        if new_score > v:
            hi_scores.remove(v)
            hi_scores.append(new_score)
            break
    hi_scores.sort()
    print(hi_scores)


leaderboard2(100)
leaderboard2(98)
