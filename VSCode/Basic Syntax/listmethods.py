"""
Built-in methods to help manipulating a list
"""

cars=['bmw', 'honda', 'audi']

length = len(cars)
print(length)

cars.append('benz')
print(cars)

cars.insert(1,'jeep')
print(cars)
# inserts an element into the list based on the index specified.

x = cars.index('honda')
print(x)
# In case there are more than one same elements in a list, this method will provide the index of only the first matching element from the list

y = cars.pop()
print(y)
print(cars)
# pop removes the last item from the list
# the list is case sensitive, ie. Jeep and jeep are considered two seperate items

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






