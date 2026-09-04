#list comprehension = a Concise way to create lists in Python

""" doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles) """

""" doubles = [x * 2 for x in range(1, 11)]
triples = [y * 2 for y in range(1, 11)]

print(doubles) """

""" fruits = ["apple", "banana"]
fruits = [fruit.upper() for fruit in fruits]

print(fruits) """

numbers = [1, -2, 3, -4]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)