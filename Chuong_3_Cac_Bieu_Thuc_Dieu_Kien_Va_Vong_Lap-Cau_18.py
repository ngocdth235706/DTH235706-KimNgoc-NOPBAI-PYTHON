n = int(input("Nhập chiều cao hình (n >= 4): "))

print("\nHình vuông rỗng:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="    ")
        else:
            print(" ", end="    ")
    print()

print("\nHình tam giác cân/tháp:")
for i in range(n):
    for j in range(n):
        if j == n - i - 1 or j == i or i == n - 1:
            print("*", end="    ")
        else:
            print(" ", end="    ")
    print()

print("\nHình chữ Z ngược/Đồ thị kết hợp:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n-i-1:
            print("*", end="    ")
        else:
            print(" ", end="    ")
    print()