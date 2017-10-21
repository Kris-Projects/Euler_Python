def isPrime(num):
    minfactor = 0
    for i in range(2, num):
        if num % i == 0:
            minfactor = i
            break

    return minfactor == num

def NthPrime(n):
    i = 0
    number = 1
    solution = 0
    while i < n:
        number += 1
        if isPrime(number):
            solution = number
            i += 1
    return solution

print(NthPrime(10001))