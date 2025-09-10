# Ví dụ về các loại lỗi và cách bắt lỗi trong Python

try:
    # Lỗi cú pháp (SyntaxError) không thể bắt bằng try-except, ví dụ: print("Hello
    # Lỗi kiểu dữ liệu (ValueError)
    so = int(input("Nhập một số nguyên: "))
    
    # Lỗi chia cho 0 (ZeroDivisionError)
    ket_qua = 10 / so
    
    # Lỗi truy cập chỉ số ngoài phạm vi (IndexError)
    ds = [1, 2, 3]
    print(ds[5])
    
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except IndexError:
    print("Lỗi: Truy cập phần tử ngoài phạm vi danh sách!")
except Exception as e:
    print("Lỗi khác:", e)