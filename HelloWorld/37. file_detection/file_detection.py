import os

file_path = "HelloWorld/37. file_detection/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesen't exists")