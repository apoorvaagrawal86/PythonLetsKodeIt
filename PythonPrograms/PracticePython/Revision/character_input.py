import datetime

name = input('Enter your name')
age = input('Enter your age')

current = datetime.datetime.now()

current_year = current.year

year_100 = current_year + (100 - int(age))

msg = ('Dear ' + str(name) + ' The year you will turn 100 is ' + str(year_100))

print(msg)

number = input('Enter the number of times you want to print the message')
for i in range(int(number)):
    print(msg)




