"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

##################################SOLUTION###############################
import math as m


def isPrime(num):
    for i in range(2, int(m.sqrt(num) + 1)):
        if num % i == 0:
            return 0
    return 1


def SumofPrime(limit):
    sumofprime = 0
    for i in range(2, limit):
        if isPrime(i):
            sumofprime += i
    return sumofprime


print(SumofPrime(2000000))
