def optimize_noun_string(s: str) -> str:
    """
    Tối ưu chuỗi danh từ:
    - Loại bỏ khoảng trắng thừa (dư, đầu/cuối)
    - Các từ cách nhau đúng 1 khoảng trắng
    - Ký tự đầu của mỗi từ viết hoa
    """
    # split() loại bỏ mọi khoảng trắng thừa, join nối lại bằng 1 dấu cách
    words = s.split()
    # capitalize() viết hoa ký tự đầu và viết thường phần còn lại
    return " ".join(w.capitalize() for w in words)

def main():
    s = input("Nhập chuỗi danh từ cần tối ưu: ")
    if not s.strip():
        print("Chuỗi rỗng.")
        return
    optimized = optimize_noun_string(s)
    print("Kết quả:", optimized)

if __name__ == "__main__":
    main()

def optimize_noun_string(s: str) -> str:
    """
    Tối ưu chuỗi danh từ:
    - Loại bỏ khoảng trắng thừa (dư, đầu/cuối)
    - Các từ cách nhau đúng 1 khoảng trắng
    - Ký tự đầu của mỗi từ viết hoa
    """
    # split() loại bỏ mọi khoảng trắng thừa, join nối lại bằng 1 dấu cách
    words = s.split()
    # capitalize() viết hoa ký tự đầu và viết thường phần còn lại
    return " ".join(w.capitalize() for w in words)

def main():
    s = input("Nhập chuỗi danh từ cần tối ưu: ")
    if not s.strip():
        print("Chuỗi rỗng.")
        return
    optimized = optimize_noun_string(s)
    print("Kết quả:", optimized)

if __name__ == "__main__":
    main()