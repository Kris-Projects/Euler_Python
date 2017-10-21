import math as m

divisors = 5
num = 7
solution = 28
while divisors <= 500:
    divisors = 2
    num += 1
    solution += num
    for i in range(2, int(m.sqrt(solution))+1):
        if solution % i == 0:
            divisors += 2

print(solution)