number = int(input('Enter the number'))
if number % 2 == 0 and number % 4 == 0:
    print(str(number) + ' is divisible by 4')
elif number % 2 == 0:
    print(str(number) + ' is even but not divisible by 4')
else:
    print(str(number) + ' is odd')

print('*'*20)

num = int(input('Enter a number'))
check = int(input('Enter another number'))
if num % check == 0:
    print(str(check) + ' divides evenly into ' + str(num))
else:
    print(str(check) + ' divides oddly into ' + str(num))




