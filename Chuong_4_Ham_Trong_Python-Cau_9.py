# ...existing code...
import math

def nested_sqrt_2(n: int) -> float:
    s = 0.0
    for _ in range(n):
        s = math.sqrt(2 + s)
    return s

def main():
    try:
        n = int(input("Nhập n (số nguyên dương): "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return

    if n <= 0:
        print("Vui lòng nhập n > 0.")
        return

    S = nested_sqrt_2(n)
    print(f"Giá trị S({n}) = {S:.6f}")

if __name__ == "__main__":
    main()
# ...existing code...