units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

n = int(input("Nhập số n (0-99): "))

if n < 0 or n > 99:
    print("Vui lòng nhập số từ 0 đến 99.")
elif n == 0:
    print("Không")
elif n < 10:
    print(units[n])
else:
    ten = n // 10
    unit = n % 10
    if ten == 1 and unit != 0:
        if unit == 5:
            print("mười lăm")
        else:
            print(f"mười {units[unit]}")
    elif unit == 0:
        print(tens[ten])
    elif unit == 5:
        print(f"{tens[ten]} lăm")
    else:
        print(f"{tens[ten]} {units[unit]}")