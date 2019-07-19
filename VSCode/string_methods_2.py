"""
Examples to show available string methods in python
"""

# Replace Method
a = '1abc2abc3abc'
print(a.replace('abc', 'ABC'))
print(a.replace('abc', 'ABC', 1))
print(a.replace('abc', 'ABC', 2))

# Sub-strings
# starting index is inclusive
# Ending index is exclusive

b=a[1]
print(b)
c = a[1:6]
print(c)
d = a[1:6:2]
print(d)

e='This is a string'
print(e)
print(e[:])
print(e[1:])
print(e[:6])
print(e[-1:])
print(e[-1])
print(e[:-1])
print(e[:len(e)])
print(e[::1])
print(e[::2])
# reverse string
print(e[::-1])
# cannot change the original string
e[1] = 'j'