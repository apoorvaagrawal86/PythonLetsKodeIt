import datetime

name = input('Enter user name')
age = int(input('Enter user age'))
current = datetime.datetime.now()
current_yr = current.year
year_100 = 100 - age + current_yr
msg = 'Dear ' + name + ' Year you will turn 100 is ' + str(year_100)
print(msg)
copies = input('Enter number of copies')
b = int(copies)


for i in range(b):
    print(msg)




