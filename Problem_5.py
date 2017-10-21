def GCD(num1, num2):
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
    if num2 == 0:
        return num1
    else:
        return GCD(num1, num2)

def LCM(num1, num2):
    product = num1 * num2
    gcd = GCD(num1, num2)
    return product // gcd

lcm = 1
for i in range(1, 21):
    lcm = LCM(lcm, i)

print(lcm)
