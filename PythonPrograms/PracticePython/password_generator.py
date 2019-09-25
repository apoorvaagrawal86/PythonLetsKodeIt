import random
import string


def pwd_gen():
    str_lower = string.ascii_lowercase
    list_lower = list(str_lower)
    print(list_lower)

    str_upper = string.ascii_uppercase
    list_upper = list(str_upper)
    print(list_upper)

    list_num = list(range(0, 10))
    print(list_num)

    str_asc = string.ascii_letters
    list_asc = list(str_asc)
    print(list_asc)

    str_sym = string.printable
    list_pri = list(str_sym)
    list_sym = list_pri[63:101]
    print(list_sym)

    a = list(list_lower[1:random.randint(1, 26)])
    b = list(list_upper[1:random.randrange(1, 26)])
    print(a, b)

    return list_lower, list_upper, list_num, list_asc, list_sym


pwd_gen()
