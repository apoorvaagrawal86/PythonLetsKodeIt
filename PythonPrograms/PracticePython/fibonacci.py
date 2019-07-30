total = int(input('Enter sequence of numbers'))
numfib = [0, 1]
for i in range(1, total):
    numfib.append(numfib[i] + numfib[i-1])
print(numfib[1:total+1])



