# Ví dụ các hàm và phương thức quan trọng trong xử lý chuỗi Python

def demo():
    s = "  Hello, Python 3! Welcome to string processing.  "
    print("Original:", repr(s))

    # cơ bản
    print("len:", len(s))
    print("strip:", repr(s.strip()))
    print("lstrip:", repr(s.lstrip()))
    print("rstrip:", repr(s.rstrip()))

    # chuyển đổi chữ hoa/thường
    print("upper:", s.upper())
    print("lower:", s.lower())
    print("title:", s.title())
    print("capitalize:", s.capitalize())
    print("swapcase:", s.swapcase())

    # tìm, đếm, thay thế
    print("find 'Python':", s.find("Python"))
    print("count 'o':", s.count("o"))
    print("replace 'Python'->'Py':", s.replace("Python", "Py"))

    # kiểm tra định dạng
    print("startswith '  He':", s.startswith("  He"))
    print("endswith '.  ':", s.endswith("  "))

    # tách và nối
    parts = s.split()
    print("split():", parts)
    print("join with '-':", "-".join(parts))

    # slicing và indexing
    print("s[2:7]:", s[2:7])
    print("s[-10:]:", s[-10:])
    print("s[::2]:", s[::2])

    # kiểm tra ký tự
    print("'123'.isdigit():", "123".isdigit())
    print("'abc'.isalpha():", "abc".isalpha())
    print("'abc123'.isalnum():", "abc123".isalnum())

    # điền bù và căn lề
    num = "42"
    print("zfill(5):", num.zfill(5))
    print("rjust(6,'.'):", num.rjust(6, '.'))
    print("center(6,'*'):", num.center(6, '*'))

    # format / f-string
    name = "An"
    score = 9.5
    print("format:", "Student: {}, score: {:.1f}".format(name, score))
    print("f-string:", f"Student: {name}, score: {score:.1f}")

if __name__ == "__main__":
    demo()