import random

b = random.randint(1, 9)
guess = 0
count = 0
# if a == b:
#    print('Exactly right')

while guess != b and guess != 'exit':
    guess = input('enter the number')

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess < b:
        print('Too low')

    elif guess > b:
        print('Too high')

    else:
        print('Exactly right!!! The correct number is ' + str(b) + 'and the number of tries is ' + count)


