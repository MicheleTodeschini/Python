 
#*args = allows to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 8, 6))

#se mettessi solo a e b e nel print mettessi 3 numeri, mi darebbe errore perché non accettati. usando * che sarebbe unpacking operator, questa cosa funziona

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_address(street="Via Pippo", city="Modena", number="9", zip_code="20125")