def random_list():
    number = int(input('Enter the number of elements you want in the list'))
    list_num = []
    while len(list_num) < number:
        a = int(input('Enter the number in the list'))
        list_num.append(a)
    print(list_num)
    return list_num


def fnl_list():
    fi_list = random_list()

    print([fi_list[0], fi_list[-1]])


fnl_list()

