"""
Built-in methods to help manipulating a list
"""

cars = ['bmw','honda','audi']

length = len(cars)
print(length)

cars.append('benz')
print(cars)

cars.insert(1,'jeep')
print(cars)

x = cars.index('honda')
print(x)
# in case there are same items in a list, it will give the index of the first item in the list

y = cars.pop()
print(y)
print(cars)
# pop removes the last item from the list
# the list is case sensitive. ie. Jeep and jeep are considered two different items.

cars.remove('jeep')
print(cars)

slicing = cars[0:2]
print(slicing)
# slicing will copy elements of a list into another.

slicing = cars[0:2]
a = cars[1:]
a = cars[1:len(a)]
print(slicing)
print(a)

cars.sort()
print(cars)
