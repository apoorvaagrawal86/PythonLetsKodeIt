a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

print('*' * 20)

list_a = []
for i in a:
    if i < 5:
        list_a.append(i)

print(list_a)

print('*' * 20)

user_num = int(input('Enter a number'))
list_b = []
for i in a:
    if i < user_num:
        list_b.append(i)
print(list_b)
