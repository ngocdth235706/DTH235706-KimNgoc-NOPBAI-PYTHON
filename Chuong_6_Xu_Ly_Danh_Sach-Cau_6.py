import random

def generate_unique_random_list(n: int, a: int, b: int) -> list[int]:
    """Trả về list gồm n số nguyên ngẫu nhiên khác nhau trong khoảng [a, b]."""
    if n < 0:
        raise ValueError("N phải >= 0")
    if b - a + 1 < n:
        raise ValueError("Khoảng giá trị quá nhỏ để tạo N số khác nhau")
    return random.sample(range(a, b + 1), n)

def main():
    try:
        n = int(input("Nhập số lượng N (số phần tử cần tạo): ").strip())
        a = int(input("Nhập giới hạn dưới a (ví dụ 0): ").strip())
        b = int(input("Nhập giới hạn trên b (ví dụ 100): ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    try:
        lst = generate_unique_random_list(n, a, b)
    except ValueError as e:
        print("Lỗi:", e)
        return

    print("Danh sách ngẫu nhiên (không trùng nhau):")
    print(lst)

if __name__ == "__main__":
    main()
    
import random

def generate_unique_random_list(n: int, a: int, b: int) -> list[int]:
    """Trả về list gồm n số nguyên ngẫu nhiên khác nhau trong khoảng [a, b]."""
    if n < 0:
        raise ValueError("N phải >= 0")
    if b - a + 1 < n:
        raise ValueError("Khoảng giá trị quá nhỏ để tạo N số khác nhau")
    return random.sample(range(a, b + 1), n)

def main():
    try:
        n = int(input("Nhập số lượng N (số phần tử cần tạo): ").strip())
        a = int(input("Nhập giới hạn dưới a (ví dụ 0): ").strip())
        b = int(input("Nhập giới hạn trên b (ví dụ 100): ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    try:
        lst = generate_unique_random_list(n, a, b)
    except ValueError as e:
        print("Lỗi:", e)
        return

    print("Danh sách ngẫu nhiên (không trùng nhau):")
    print(lst)

if __name__ == "__main__":
    main()