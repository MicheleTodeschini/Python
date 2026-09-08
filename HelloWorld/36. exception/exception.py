
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")