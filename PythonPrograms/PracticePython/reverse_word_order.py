def rev_string():
    str_a = input('Enter a sentence')
    str_b = str_a.split()
    str_b = list(str_b)
    print(str_b)
    str_c = str_b[::-1]
    print(str_c)
    return str_c


rev_string()