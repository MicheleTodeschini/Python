#input() = Una funzione che fa inserire dati all'utente, restituisce i dati sotto forma di stringa

name = input('Come ti chiami?: ')
age = int(input('Quanti anni hai?:' )) 


# AL POSTO DI METTERE INT DOPO AGE RIGA 4 POSSO FARE COSì MA IMPIEGO PIù CODICE
age = int(age)
age = age + 1 

print(f'Hello {name}')
print('Auguriiiii')
print(f'Hai {age} anni')
 
