import random

# Các giá trị có thể xuất hiện khi chạy randrange(0, 100) là các số nguyên từ 0 đến 99 (bao gồm 0, không bao gồm 100)
print("Ví dụ giá trị ngẫu nhiên:", random.randrange(0, 100))

# Kiểm tra các giá trị:
test_values = [4.5, 34, -1, 100, 0, 99]
for val in test_values:
    if isinstance(val, int) and 0 <= val < 100:
        print(f"{val} có thể xuất hiện trong randrange(0, 100)")
    else:
        print(f"{val} không thể xuất hiện trong randrange(0, 100)")