number = int(input('Enter a number'))


def prime_number(number):
    if number == 2:
        prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
        else:
            prime = True
    return prime


if prime_number(number) == True:
    print('Number is prime')
else:
    print('Number is not prime')


