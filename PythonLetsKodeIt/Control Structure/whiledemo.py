"""
Execute statements repeatedly
conditions are used to stop the execution of loop
Iterable items are strings, list, tuple, dictionary
"""

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

l = []
num = 0
while num < 10:
    l.append(num)
    num += 1
    print("value of num is: " + str(num))
print(l)