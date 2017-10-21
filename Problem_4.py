def Palintest(number):
    temp1 = str(number)
    temp2 = temp1[::-1]
    return temp1 == temp2

solution = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if Palintest(product) and solution < product:
            solution = product

print(solution)
