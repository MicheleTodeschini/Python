# indexing = accessing elemtns of a sequence using []

credit_number = '1234-5678-9012-3456'

# print(credit_number[1])

# print(credit_number[0:4]) da 0 compreso a 4 escluso

# print(credit_number[5:9])

# print(credit_number[5:])

# print(credit_number[-3]) va anche in negativo

#  print(credit_number[::2])  stampa tutti a numeri alterni

last_digit = credit_number[-4:] #prende dagli ultimi 4 fino alla fine

print(f'XXXX_XXXX_XXXX_{last_digit}')