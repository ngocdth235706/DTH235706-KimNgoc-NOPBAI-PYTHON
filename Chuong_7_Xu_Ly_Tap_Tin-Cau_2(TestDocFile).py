from Chuong_7_Xu_Ly_Tap_Tin_Cau_2XuLyFile import *
arrSo=DocFile("csdl_so.txt")
print(arrSo)
def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number=int(element)
            if number<0:
                print(number,end='\t')
        print()
print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)