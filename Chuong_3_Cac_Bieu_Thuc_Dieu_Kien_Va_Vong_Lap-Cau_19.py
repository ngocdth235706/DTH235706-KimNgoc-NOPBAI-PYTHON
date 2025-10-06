import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = x
for k in range(1, n + 1):
    S += x ** (2 * k + 1) / math.factorial(2 * k + 1)

print("Giá trị S(x, n) =", S)