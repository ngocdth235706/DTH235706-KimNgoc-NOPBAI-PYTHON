# Nhập một chuỗi từ bàn phím
ten = input("Nhập tên của bạn: ")
print("Tên bạn vừa nhập là:", ten)

# Nhập một số nguyên
tuoi = int(input("Nhập tuổi của bạn: "))
print("Tuổi bạn vừa nhập là:", tuoi)

# Nhập một số thực
diem = float(input("Nhập điểm của bạn: "))
print("Điểm bạn vừa nhập là:", diem)

# Nhập nhiều giá trị trên một dòng, cách nhau bởi dấu cách
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
a = int(a)
b = int(b)
print("Hai số bạn vừa nhập là:", a, "và", b)