import tkinter as tk
from tkinter import messagebox

# Công thức chuyển đổi từ Fahrenheit sang Celsius: C = (F - 32) * 5/9
def convert_f_to_c():
    """
    Hàm thực hiện việc lấy giá trị độ F, tính toán, và hiển thị kết quả độ C.
    """
    try:
        # Lấy giá trị độ F từ ô nhập liệu
        f_str = entry_f.get()
        if not f_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập giá trị độ F.")
            # Xóa nội dung kết quả cũ nếu có lỗi
            label_c_result.config(text="Độ C ở đây")
            return

        # Chuyển đổi sang số thực (float) để tính toán chính xác
        fahrenheit = float(f_str)
        
        # Áp dụng công thức chuyển đổi
        # C = (F - 32) * 5/9
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        
        # Làm tròn kết quả đến 2 chữ số thập phân
        celsius_rounded = round(celsius, 2)
        
        # Định dạng và hiển thị kết quả lên giao diện
        result_text = f"{celsius_rounded}°C"
        label_c_result.config(text=result_text, fg='blue', font=('Arial', 14, 'bold'))

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ cho nhiệt độ.")
        label_c_result.config(text="Độ C ở đây", fg='black', font=('Arial', 12))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")


# --- Thiết lập Giao diện Tkinter ---

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi °F sang °C")

# Tạo Frame bao bọc, đặt màu vàng như hình
main_frame = tk.Frame(root, bg="#FFFF00", padx=30, pady=30, bd=5, relief="raised")
main_frame.pack(padx=20, pady=20)

# 1. Hàng Nhập độ F
label_f = tk.Label(main_frame, text="Nhập độ F", bg="#FFFF00", font=('Arial', 14))
label_f.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Ô nhập liệu (Entry)
entry_f = tk.Entry(main_frame, width=8, justify='center', font=('Arial', 14))
entry_f.insert(0, "350") # Đặt giá trị mặc định là 350
entry_f.grid(row=0, column=1, padx=10, pady=10)

# 2. Hàng Nút Chuyển
# Nút "Chuyển"
button_convert = tk.Button(
    main_frame, 
    text="Chuyển", 
    command=convert_f_to_c, # Liên kết với hàm tính toán
    font=('Arial', 12, 'bold'), 
    fg='white', 
    bg='#007FFF', # Màu xanh dương
    relief='raised', 
    bd=4
)
button_convert.grid(row=1, column=1, padx=10, pady=10, sticky='n')

# 3. Hàng Kết quả Độ C
label_c_text = tk.Label(main_frame, text="Độ C", bg="#FFFF00", font=('Arial', 14))
label_c_text.grid(row=2, column=0, padx=10, pady=10, sticky='w')

# Nhãn hiển thị kết quả
label_c_result = tk.Label(main_frame, text="Độ C ở đây", bg="#FFFF00", font=('Arial', 12))
label_c_result.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Chạy tính toán lần đầu với giá trị mặc định "350"
convert_f_to_c()

# Khởi chạy vòng lặp chính của giao diện
root.mainloop()