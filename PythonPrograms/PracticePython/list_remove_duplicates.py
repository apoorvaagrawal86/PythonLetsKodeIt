list_a = []
number = int(input('Enter the number of elements you want in the list'))
while len(list_a) < number:
    n = int(input('Enter the number in list'))
    list_a.append(n)
print('list a is ' + str(list_a))
list_c = list_a
list_b = []
count = 0
for i in list_a:
    count = count + 1
    print('value of i is ' + str(i))
    print('count is ' + str(count))
    print('list_a is ' + str(list_a[count:number]))
    if i in list_a[count:number]:
        list_b.append(i)
        print('list_b is ' + str(list_b))
print('list_b is ' + str(list_b))


