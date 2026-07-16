import random

options = ('rock', 'paper', 'scissors')
player = None
computer = random.choice(options)

while player not in options:
    player = input('enter a choice (rock, paper, scissors): ')

print(f'player: {player}') 
print(f'computer: {computer}')

if player == computer:
    print('Its a tie')
elif player == 'rock' and computer == 'scissors':
    print('You win')
elif player == 'paper' and computer == 'rock':
    print('You win!')
elif player == 'scissors' and computer == 'paper':
    print('You win!')
else:
    print('you lose :(')