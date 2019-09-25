def largest_num(*args):
    print(max(args))


largest_num(-20, -10, 0, 10, 100)


def smallest_num(*args):
    print(min(args))
    return min(args)


x = smallest_num(-20, -10, 0, 10, 100)


def abs_function(a):
    print(abs(a))


abs_function(-20)
abs_function(20)


print(type(99))
print(type(99.9))
print(type('99.9'))

l = [1, 2, 3]
print(type(l))
