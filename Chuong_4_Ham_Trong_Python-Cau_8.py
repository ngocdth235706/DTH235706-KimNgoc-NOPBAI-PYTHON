import math

x = float(input("Nhập x (>0): "))
a = float(input("Nhập a (>0, a != 1): "))

if x > 0 and a > 0 and a != 1:
    log_a_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) =", log_a_x)
else:
    print("Giá trị x phải > 0, a phải > 0 và a != 1.")