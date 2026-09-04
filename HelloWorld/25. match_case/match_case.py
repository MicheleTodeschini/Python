def number(num):
    match num:
        case 1:
            return "1"
        case 2:
            return "2"
        case _:
            return "Not a valid number"


print(number(1))