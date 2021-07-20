from itertools import combinations
scores = [40, 91, 85, 15]

result = list(combinations(scores, 2))
print(result)

# Without libraries:

for i in range(len(scores)):
    for j in range(i+1, len(scores)):
        print(scores[i], scores[j])


s = "i_love_programming_in_python_and_i_will_alzways_program".split("_")
uniques = []
s2 = "".join(s)
# print(s2)

for char in s2:
    if char not in uniques:
        uniques.append(char)
print("".join(uniques))
