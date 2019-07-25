pal = str(input('Enter the string'))
pal = pal.lower()
print(pal)

pal_rev = pal[::-1]

if pal_rev == pal:
    print('String is palindrome')
else:
    print('String is not a palindrome')

# pal_copy = pal[:]
# print(pal_copy)

# pal.reverse()

# print(pal)

# for i in pal_copy:
#    for j in pal:
#        if i == j:
#            print('String is palindrome')
#        else:
#            print('String is not a palindrome')

# if pal == pal_copy:
#    print('String is a pallindrome')
# else:
#    print('String is not a pallindrome')