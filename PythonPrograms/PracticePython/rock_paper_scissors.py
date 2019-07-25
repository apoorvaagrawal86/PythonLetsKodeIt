a = input('Enter player 1 choice')
b = input('Enter player 2 choice')

while a == 'rock':
    if b == 'scissors':
        print('Player A wins')
    elif b == 'paper':
        print('Player B wins')
    else:
        print('Its a tie, try again')
    break
while a == 'scissors':
    if b == 'paper':
        print('Player A wins')
    elif b == 'rock':
        print('Player B wins')
    else:
        print('Its a tie, try again')
    break
while a == 'paper':
    if b == 'rock':
        print('Player A wins')
    elif b == 'scissors':
        print('Player B wins')
    else:
        print('Its a tie, try again')
    break

