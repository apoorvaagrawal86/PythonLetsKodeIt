list_a = []
number = int(input('Enter the number of elements you want in the list'))
while len(list_a) < number:
    i = int(input('Enter the number you want in the list'))
    list_a.append(i)
print(list_a)

print(set(list_a))



