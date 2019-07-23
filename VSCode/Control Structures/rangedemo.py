"""
Built-in function
Creates a sequence of number but does not save them in memory
Very useful for generating numbers
"""

print(list(range(0,10)))

a=range(0,20,4)
print(a)
print(type(a))
print(list(a))

for num in range(3):
    print(num)