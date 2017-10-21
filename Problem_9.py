"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

###################################SOLUTION####################################

for i in range(3, 998):
    for j in range(1, i):
        if (i * i == j * j + (1000 - i - j) ** 2):
            print(i*j*(1000-i-j))