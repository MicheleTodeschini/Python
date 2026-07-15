# build a figure using nested loops

rows = int(input('enter the numbers of rows: '))
column = int(input('enter the numbers of column: '))
symbol = input('enter the symbol to use: ')

for i in range(rows):
    for x in range(column):
        print(symbol, end='')
    print()