def create_list():
    number = int(input('Enter the number of elements you want in the list'))
    list_a = []
    while len(list_a) < number:
        i = int(input('Enter the number in the list'))
        list_a.append(i)
    print(list_a)
    list_c = []
    count = 1
    for j in list_a:
        count = count + 1
        if j not in list_a[count:number]:
            list_c.append(j)
    print(list_c)
    return list_c


# create_list()


def list_sets():
    number = int(input('Enter the number of elements you want in the list'))
    list_a = []
    while len(list_a) < number:
        i = int(input('Enter the number in the list'))
        list_a.append(i)
    print(list_a)
    list_a = set(list_a)
    # list_a = set(list_a)
    # print(list_a)
    return list_a


print(list_sets())
# def no_duplicate_list():
#     global list_a
#     list_b = list_a
#     count = 0
#     list_c = []
#     for j in list_b:
#         count = count + 1
#         if j not in list_b[count + 1:len(list_b)]:
#             list_c.append(j)
#     print(list_c)
#     return list_c
#
#
# no_duplicate_list()
