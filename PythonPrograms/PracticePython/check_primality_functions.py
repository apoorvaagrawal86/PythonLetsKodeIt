a = int(input('Enter a number'))
b = []
c = []
for i in range(2, a + 1):
    if a % i == 0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)

if len(b) == 1:
    print(str(a) + ' is a prime number')
else:
    print(str(a) + ' is a composite number')


