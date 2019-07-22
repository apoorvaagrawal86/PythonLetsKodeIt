"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x < 10:
    print("value of x is: " + str(x))
    x = x + 1

    if x == 8:
        break
    print("This example is awesome")
    print("*" * 20)
else:
    print("Outside the loop")

x = 0
while x < 10:
    print("value of x is: " + str(x))
    x = x + 1

    if x == 8:
        continue
    print("This example is awesome")
    print("*" * 20)

print("Outside the loop")


