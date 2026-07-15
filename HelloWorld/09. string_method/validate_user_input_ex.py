# validate user input
#1. username is no more than 12 characters
#2. username must no t contain spaces
#3. username must not contain digits

username = input('Enter a usernmae: ')




if len(username) > 12:
    print('Username nono be more than 12 characters')
elif not username.find(' ') == -1:
    print('Your username non può contain spaces')
elif username.isalpha() == False:
    print('No number, only characters')
else:
    print(f'Welcome {username}')

