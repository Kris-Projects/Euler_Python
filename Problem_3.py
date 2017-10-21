def getMinFactor(sourceValue):
    minfactor = 0
    for i in range(2, int(sourceValue / 2) + 2):
        if sourceValue % i == 0:
            minfactor = i
            break

    return minfactor

number = 600851475143
maxFactor = 0
factor = getMinFactor(number)

while factor > 0:
    print(factor)
    number /= factor
    factor = getMinFactor(number)

    if factor > maxFactor:
        maxFactor = factor

print(number)
if number > maxFactor:
    maxFactor = number

print('max factor:', maxFactor)