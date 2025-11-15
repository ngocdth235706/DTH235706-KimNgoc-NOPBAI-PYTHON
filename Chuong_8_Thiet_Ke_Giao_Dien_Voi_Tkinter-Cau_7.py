import tkinter as tk
from tkinter import messagebox

# 1. Định nghĩa các mảng Thiên Can và Địa Chi
# Thiên Can (Can) - 10 yếu tố
CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]

# Địa Chi (Chi) - 12 yếu tố
CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def convert_solar_to_lunar():
    """
    Hàm chuyển đổi năm Dương lịch sang Âm lịch (Can Chi).
    """
    try:
        # Lấy giá trị năm dương lịch từ ô nhập liệu
        solar_year_str = entry_solar_year.get()
        if not solar_year_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập năm Dương lịch.")
            return

        solar_year = int(solar_year_str)
        
        # 2. Tính toán Thiên Can (Can)
        # Công thức: (Năm - 3) % 10. Giá trị này sẽ là index của CAN.
        # Ví dụ: Năm 1982
        # (1982 - 3) = 1979
        # 1979 % 10 = 9. Index 9 trong CAN là "Kỷ" (Nhâm Tuất thì Can là Nhâm, lỗi logic ở đây)
        
        # Cập nhật công thức: Canh Tý (0) = 1960. Hoặc đơn giản hơn:
        # Index Can = (Năm - X) % 10, với X là một hằng số điều chỉnh để 1982 ra Nhâm (index 2)
        # Giả sử 1982 là Nhâm Tuất:
        # 1982 % 10 = 2 (Canh, Tân, Nhâm) -> CAN[2] = Nhâm.
        # Chúng ta có thể dùng CAN[Năm % 10] nếu danh sách CAN được sắp xếp lại.
        
        # Dùng mảng CAN có thứ tự chuẩn: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
        # Và công thức: Index Can = (Năm - 3) % 10
        
        # Index Can = (Năm - 3) % 10
        # Index Chi = (Năm - 3) % 12
        
        # Sắp xếp lại CAN và CHI để phù hợp với công thức trên:
        CAN_ADJ = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
        CHI_ADJ = ["Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]
        
        # Index Thiên Can
        index_can = (solar_year % 10)
        
        # Index Địa Chi
        index_chi = (solar_year % 12)
        
        # Lấy Thiên Can và Địa Chi tương ứng
        # 1982: Canh Tuất. 1982 % 10 = 2. 1982 % 12 = 2.
        # Để 1982 ra Nhâm Tuất (theo hình):
        # Ta phải điều chỉnh index. Giả sử 1982 là Nhâm Tuất.
        # Can (1982) là Nhâm -> Index 2 (của CAN chuẩn: Giáp(0), Ất(1), Bính(2), Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý) -> (1982 - 2) % 10 = 0.
        
        # SỬ DỤNG CÔNG THỨC CHUẨN ĐƯỢC CHỨNG MINH (Phù hợp với CAN/CHI đã sắp xếp):
        # Canh (7) (1980) là Canh Thân
        # Tân (8) (1981) là Tân Dậu
        # Nhâm (9) (1982) là Nhâm Tuất -> Đúng như hình.
        
        # Can: (Năm - 4) % 10. Ví dụ: (1982 - 4) = 1978. 1978 % 10 = 8. CAN[8] là Nhâm.
        # Chi: (Năm - 4) % 12. Ví dụ: (1982 - 4) = 1978. 1978 % 12 = 10. CHI[10] là Tuất.
        # Danh sách CAN và CHI phải được sắp xếp lại từ Giáp/Tý
        
        # 3. Mảng CAN và CHI được sắp xếp theo thứ tự chuẩn bắt đầu từ Giáp Tý (index 0)
        CAN_STT = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"] # Giáp (0) -> Quý (9)
        CHI_STT = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"] # Tý (0) -> Hợi (11)

        # Công thức chuẩn để tính Can và Chi từ năm Dương lịch:
        # Index Can = (Năm Dương lịch - 3) % 10. (Vì 0 là Giáp, năm 4 là Giáp)
        # Index Chi = (Năm Dương lịch - 3) % 12. (Vì 0 là Tý, năm 4 là Tý)
        
        index_can = (solar_year + 6) % 10
        index_chi = (solar_year + 8) % 12
        
        # Năm 1982:
        # Index Can: (1982 + 6) % 10 = 1988 % 10 = 8. CAN_STT[8] = "Nhâm"
        # Index Chi: (1982 + 8) % 12 = 1990 % 12 = 10. CHI_STT[10] = "Tuất"
        
        can = CAN_STT[index_can]
        chi = CHI_STT[index_chi]
        
        lunar_year = f"{can} {chi}"
        
        # 4. Hiển thị kết quả lên giao diện
        label_lunar_year.config(text=lunar_year)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ cho năm.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# --- Thiết lập Giao diện Tkinter ---

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi Dương Lịch - Âm Lịch")

# Tạo Frame bao bọc, đặt màu vàng như hình
main_frame = tk.Frame(root, bg="#FFFF00", padx=30, pady=30, bd=5, relief="raised")
main_frame.pack(padx=20, pady=20)

# --- Hàng 1: Nhập năm Dương ---
label_solar_year = tk.Label(main_frame, text="Nhập năm dương:", bg="#FFFF00", font=('Arial', 14))
label_solar_year.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Ô nhập liệu (Entry)
entry_solar_year = tk.Entry(main_frame, width=8, justify='center', font=('Arial', 14, 'bold'), fg='red')
entry_solar_year.insert(0, "1982") # Đặt giá trị mặc định là 1982
entry_solar_year.grid(row=0, column=1, padx=10, pady=10)

# --- Hàng 2: Nút Chuyển ---
# Nút "Chuyển"
button_convert = tk.Button(main_frame, text="Chuyển", command=convert_solar_to_lunar, font=('Arial', 12, 'bold'), fg='white', bg='blue', relief='raised', bd=4)
button_convert.grid(row=1, column=1, padx=10, pady=10, sticky='n')

# --- Hàng 3: Kết quả Năm Âm ---
label_lunar_text = tk.Label(main_frame, text="Năm âm:", bg="#FFFF00", font=('Arial', 14))
label_lunar_text.grid(row=2, column=0, padx=10, pady=10, sticky='w')

# Nhãn hiển thị kết quả (Label)
label_lunar_year = tk.Label(main_frame, text="Nhâm Tuất", bg="#FFFF00", font=('Arial', 14, 'bold'))
# Gọi hàm chuyển đổi lần đầu để hiển thị kết quả mặc định
convert_solar_to_lunar()
label_lunar_year.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Khởi chạy vòng lặp chính của giao diện
root.mainloop()