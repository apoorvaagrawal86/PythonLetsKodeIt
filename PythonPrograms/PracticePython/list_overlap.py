import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(c)

print('*' * 20)

d = range(1, random.randint(1,30))
e = range(1, random.randint(10, 40))
f = []

print(d)
print(e)
for i in d:
    if i in e:
        if i not in f:
            f.append(i)
print(f)

