"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
#################################SOLUTION##################################
product = 1
for i in range(1, 101):
    product *= i

sum = 0
for j in str(product):
    sum += int(j)

print(sum)