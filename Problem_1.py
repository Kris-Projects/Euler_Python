sumofmul = 0

for i in range(1, 1000):
    if i % 3 == 0:
        sumofmul += i
    elif i % 5 == 0:
        sumofmul += i
    else:
        continue

print(sumofmul)