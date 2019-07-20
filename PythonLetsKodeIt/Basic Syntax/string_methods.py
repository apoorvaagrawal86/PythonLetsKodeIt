"""
Examples to show available string methods in python
"""

# Accessing characters in a string
# Index starts from zero
first = "nyc"[0]
city = 'sfo'
print(first)
ft = city[0]
print(ft)

"""
len()
lower()
upper()
str()
"""

string = "This is a Mixed Case"
print(string.lower())
print(string.upper())
print(len(string))

print(string + str(2))

"""
concatenation of strings
"""
print("Hello " + " " + " World!!!")

print(first + " " + city)