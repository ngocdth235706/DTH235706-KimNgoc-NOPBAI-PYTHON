import tkinter as tk
from tkinter import messagebox

# Định nghĩa các ngưỡng và kết quả tương ứng
# Lưu ý: Bảng chỉ có 4 mức. Chúng ta cần bổ sung Nguy cơ phát triển bệnh.
# Dựa trên hình ảnh, "Hơi Béo" có vẻ nằm giữa "Mập" (25-29.9) và "Béo phì" (>=30)
# Giả sử: 
# "Hơi Béo" = 25.0 - 29.9 (Mập)
# "Nguy cơ phát triển bệnh":
#   - Thấp: < 25.0
#   - Hơi hơi cao (Trung bình/Cao): 25.0 - 29.9
#   - Rất cao: >= 30.0

def calculate_bmi_and_classify():
    """
    Hàm tính toán BMI, phân loại tình trạng cân nặng và nguy cơ bệnh.
    """
    try:
        # 1. Lấy dữ liệu từ ô nhập liệu
        height_str = entry_height.get()
        weight_str = entry_weight.get()

        if not height_str or not weight_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ Chiều cao và Cân nặng.")
            return

        # Chiều cao (m) và Cân nặng (kg)
        height = float(height_str)
        weight = float(weight_str)

        if height <= 0 or weight <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và Cân nặng phải là giá trị dương.")
            return

        # 2. Tính chỉ số BMI
        # Công thức: BMI = Weight / (Height * Height)
        bmi = weight / (height ** 2)
        bmi_rounded = round(bmi, 2)

        # 3. Phân loại Tình trạng cân nặng
        status = ""
        risk = ""

        if bmi < 18.5:
            status = "Gầy"
            risk = "Thấp"
        elif 18.5 <= bmi <= 24.9:
            status = "Bình thường"
            risk = "Thấp"
        elif 25.0 <= bmi <= 29.9:
            # Dựa vào hình, ta dùng "Hơi Béo" cho khoảng này
            status = "Hơi Béo (Mập)"
            risk = "Hơi hơi cao"
        else: # bmi >= 30.0
            status = "Béo phì"
            risk = "Cao"
            
        # 4. Cập nhật kết quả lên giao diện
        entry_bmi.config(state=tk.NORMAL) # Mở khóa để cập nhật
        entry_status.config(state=tk.NORMAL)
        entry_risk.config(state=tk.NORMAL)
        
        entry_bmi.delete(0, tk.END)
        entry_bmi.insert(0, str(bmi_rounded))
        
        entry_status.delete(0, tk.END)
        entry_status.insert(0, status)
        
        entry_risk.delete(0, tk.END)
        entry_risk.insert(0, risk)
        
        entry_bmi.config(state='readonly') # Khóa lại
        entry_status.config(state='readonly')
        entry_risk.config(state='readonly')

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho Chiều cao và Cân nặng.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

def quit_app():
    """Hàm thoát ứng dụng."""
    root.quit()

# --- Thiết lập Giao diện Tkinter ---

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Phần mềm tính chỉ số BMI")

# Tạo Frame bao bọc, đặt màu vàng như hình
main_frame = tk.Frame(root, bg="#FFFF00", padx=30, pady=30, bd=5, relief="raised")
main_frame.pack(padx=20, pady=20)

# --- Định nghĩa các widget ---

# Danh sách các nhãn (Labels)
labels = [
    "Nhập chiều cao:", 
    "Nhập cân nặng:", 
    "BMI của bạn:", 
    "Tình trạng của bạn:", 
    "Nguy cơ phát triển bệnh"
]

# Danh sách các ô nhập/hiển thị (Entries)
# Dùng Dictionary để dễ dàng tham chiếu
entries = {} 

# --- Vòng lặp tạo giao diện ---
for i, text in enumerate(labels):
    # Tạo nhãn ở cột 0
    label = tk.Label(main_frame, text=text, bg="#FFFF00", font=('Arial', 12))
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    
    # Tạo Entry ở cột 1
    entry = tk.Entry(main_frame, width=15, justify='center', font=('Arial', 12, 'bold'))
    entry.grid(row=i, column=1, padx=10, pady=5)
    
    # Lưu Entry vào dictionary để dễ truy cập sau này
    if text == "Nhập chiều cao:":
        entry_height = entry
        entry.insert(0, "1.8") # Giá trị mặc định
    elif text == "Nhập cân nặng:":
        entry_weight = entry
        entry.insert(0, "172") # Giá trị mặc định
    elif text == "BMI của bạn:":
        entry_bmi = entry
        entry.insert(0, "x")
        entry.config(state='readonly') # Chỉ hiển thị, không cho nhập
    elif text == "Tình trạng của bạn:":
        entry_status = entry
        entry.insert(0, "Hơi Béo")
        entry.config(state='readonly')
    elif text == "Nguy cơ phát triển bệnh":
        entry_risk = entry
        entry.insert(0, "Hơi hơi cao")
        entry.config(state='readonly')


# --- Nút "Tính BMI" ---
button_calc = tk.Button(
    main_frame, 
    text="Tính BMI", 
    command=calculate_bmi_and_classify, # Liên kết với hàm tính toán
    font=('Arial', 12, 'bold'), 
    fg='white', 
    bg='#007FFF', 
    relief='raised', 
    bd=4
)
button_calc.grid(row=len(labels), column=1, padx=10, pady=10, sticky='ew') # Đặt dưới cùng

# --- Nút "Thoát" ---
button_quit = tk.Button(
    main_frame, 
    text="Thoát", 
    command=quit_app,
    font=('Arial', 12, 'bold'), 
    fg='white', 
    bg='red', 
    relief='raised', 
    bd=4
)
button_quit.grid(row=len(labels) + 1, column=1, padx=10, pady=10, sticky='ew')

# Chạy tính toán lần đầu với giá trị mặc định để hiển thị kết quả ban đầu
calculate_bmi_and_classify()

# Khởi chạy vòng lặp chính của giao diện
root.mainloop()