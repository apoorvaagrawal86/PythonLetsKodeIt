def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, 8)
sum2 = sum_nums(3, 3)

print(sum1)
print('*' * 20)


def is_metro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False


x = is_metro('bos')
print(x)
