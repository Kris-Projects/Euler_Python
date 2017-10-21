def Fibgen(limit):
    fib = [1, 2]
    while True:
        temp = fib[-1] + fib[-2]
        if temp <= limit:
            fib.append(temp)
        else:
            break

    return fib

fib_test = Fibgen(4000000)
fib_even = list(filter(lambda x: x%2==0, fib_test))
print(sum(fib_even))

