num = int(input('Enter a number'))

if num % 4 == 0:
    print(str(num) + ' is divisible by 4')
elif num % 2 == 0:
    print(str(num) + ' is divisible by 2')
else:
    print(str(num) + ' is odd')

check = int(input('Enter the number to divide by num'))

if num%check == 0:
    print(str(num) + ' divides evenly into ' + str(check))
else:
    print(str(num) + ' divides oddly into ' + str(check))
