"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, list, tuple, dictionary
"""

my_string = "abcabc"

for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print()

cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car)

nums = [1,2,3]
for n in nums:
    print(n*10)

print('*'*20)

d = {'one':1, 'two':2, 'three':3}
for k in d:
    print(k + ' ' + str(d[k]))

print('*' * 20)

for k,v in d.items():
    print(k)
    print(v)






