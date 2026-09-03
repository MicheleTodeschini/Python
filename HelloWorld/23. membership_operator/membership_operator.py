# Membership Operator is used to test wheter a value or a variable is found in a sequence
# in oppure not in

""" 
word = "APPLE"

letter = input("Guess a letter in the secred word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found") """

""" students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")
 """

grades = {"Sandy": "A", 
          "Spongebob": "B"}

student = input("Enter the name of a student")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")