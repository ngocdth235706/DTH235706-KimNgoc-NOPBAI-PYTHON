import math

xA = float(input("Nhập hoành độ điểm A: "))
yA = float(input("Nhập tung độ điểm A: "))
xB = float(input("Nhập hoành độ điểm B: "))
yB = float(input("Nhập tung độ điểm B: "))

dAB = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print("Độ dài đoạn AB là:", dAB)
