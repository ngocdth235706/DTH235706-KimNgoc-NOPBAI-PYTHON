# Ba hàm và 3 trường hợp kiểm tra kết quả như trong ảnh

def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

def main():
    global val

    # Trường hợp 1:
    # val = 5
    # print(sum1(5))
    # print(sum2())
    # print(sum3())
    val = 5
    print("Trường hợp 1:")
    print("sum1(5) ->", sum1(5))   # 5
    print("sum2()  ->", sum2())    # 5, val giảm về 0
    print("sum3()  ->", sum3())    # 0 (vì val == 0)
    print()

    # Trường hợp 2:
    # val = 5
    # print(sum1(5))
    # print(sum3())
    # print(sum2())
    val = 5
    print("Trường hợp 2:")
    print("sum1(5) ->", sum1(5))   # 5
    print("sum3()  ->", sum3())    # 5 (val vẫn 5)
    print("sum2()  ->", sum2())    # 5, val giảm về 0
    print()

    # Trường hợp 3:
    # val = 5
    # print(sum2())
    # print(sum1(5))
    # print(sum3())
    val = 5
    print("Trường hợp 3:")
    print("sum2()  ->", sum2())    # 5, val giảm về 0
    print("sum1(5) ->", sum1(5))   # 5
    print("sum3()  ->", sum3())    # 0 (val == 0)

if __name__ == "__main__":
    main()
    