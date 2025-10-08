import math

n = int(input("Nhập n: "))
S = 0
for _ in range(n):
    S = math.sqrt(2 + S)
print("Giá trị S(n) =", S)