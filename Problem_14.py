len_max = 0
result = 0
for digit in range(1, 1000000):
    i = digit
    count = 1
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        count += 1

    if len_max < count:
        len_max = count
        result = digit

print(result)