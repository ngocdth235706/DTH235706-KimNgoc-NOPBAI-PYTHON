from Chuong_7_Xu_Ly_Tap_Tin_Cau_1_XuLyFile import *

masp=input("nhập mã SP:")
tensp=input("nhập tên sp:")
dongia=float(input("nhập giá:"))
line=masp+";"+tensp+";"+str(dongia)

LuuFile("database.txt",line)