import math

def sum_proper_divisors(n: int) -> int:
    """Trả về tổng các ước dương của n (không kể chính n)."""
    if n <= 1:
        return 0
    s = 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s

def is_perfect(n: int) -> bool:
    """True nếu n là số hoàn thiện (perfect)."""
    return n > 1 and sum_proper_divisors(n) == n

def is_abundant(n: int) -> bool:
    """True nếu n là số thịnh vượng (abundant)."""
    return sum_proper_divisors(n) > n

def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return

    if n <= 0:
        print("Vui lòng nhập n > 0.")
        return

    s = sum_proper_divisors(n)
    print(f"Tổng các ước (không kể {n}) = {s}")

    if is_perfect(n):
        print(f"{n} là số hoàn thiện (Perfect number).")
    elif is_abundant(n):
        print(f"{n} là số thịnh vượng (Abundant number).")
    else:
        print(f"{n} là số khiếm khuyết (Deficient number).")

if __name__ == "__main__":
    main()
# filepath: d:\Python\-Th-Kim-Ng-c_DTH235706_L-p-tr-nh-Python\Chuong_4_Ham_Trong_Python-Cau_13.py
import math

def sum_proper_divisors(n: int) -> int:
    """Trả về tổng các ước dương của n (không kể chính n)."""
    if n <= 1:
        return 0
    s = 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s

def is_perfect(n: int) -> bool:
    """True nếu n là số hoàn thiện (perfect)."""
    return n > 1 and sum_proper_divisors(n) == n

def is_abundant(n: int) -> bool:
    """True nếu n là số thịnh vượng (abundant)."""
    return sum_proper_divisors(n) > n

def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return

    if n <= 0:
        print("Vui lòng nhập n > 0.")
        return

    s = sum_proper_divisors(n)
    print(f"Tổng các ước (không kể {n}) = {s}")

    if is_perfect(n):
        print(f"{n} là số hoàn thiện (Perfect number).")
    elif is_abundant(n):
        print(f"{n} là số thịnh vượng (Abundant number).")
    else:
        print(f"{n} là số khiếm khuyết (Deficient number).")

if __name__ == "__main__":
    main()