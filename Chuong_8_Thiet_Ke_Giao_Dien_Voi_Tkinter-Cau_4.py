import pandas as pd
from os import path
from tkinter import *

# --- KHAI BÁO BIẾN TOÀN CỤC ---
root = Tk()
root.title("Simple Calculator")

# Biến để lưu trữ biểu thức hiện tại
expression = "" 
# Biến Stringvar để hiển thị kết quả/biểu thức
text_input = StringVar() 

# --- HÀM XỬ LÝ SỰ KIỆN ---
def click_button(item):
    """Xử lý khi nhấn các nút số, dấu thập phân và phép toán."""
    global expression
    expression = expression + str(item)
    text_input.set(expression)

def clear_button():
    """Xóa toàn bộ biểu thức."""
    global expression
    expression = ""
    text_input.set("")

def equals_button():
    """Tính toán kết quả của biểu thức."""
    global expression
    try:
        # Sử dụng eval() để tính toán biểu thức chuỗi
        result = str(eval(expression))
        text_input.set(result)
        expression = result # Giữ kết quả để tiếp tục tính toán
    except ZeroDivisionError:
        text_input.set("Error: Div by zero")
        expression = ""
    except Exception:
        text_input.set("Error")
        expression = ""

# --- THIẾT KẾ GIAO DIỆN ---

# Khung hiển thị (Entry)
input_field = Entry(root, textvariable=text_input, bd=5, insertwidth=4, width=20, 
                    font=('Arial', 16), justify='right')
input_field.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Khung chứa các nút bấm
btns_frame = Frame(root)
btns_frame.grid(row=1, column=0, columnspan=3)

# Định nghĩa các nút (số, dấu)
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '-', '0', '.',
]

# Định nghĩa các nút phép toán và chức năng
operations = [
    '+', '-', '*', '/',
]

# Thêm các nút số và dấu thập phân vào lưới
row_val = 0
col_val = 0
for button in buttons:
    Button(btns_frame, text=button, padx=10, pady=10, 
           command=lambda item=button: click_button(item)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Thêm các nút phép toán và Clr
row_val = 4
col_val = 0
for op in operations:
    Button(btns_frame, text=op, padx=10, pady=10, bg="#f0f0f0",
           command=lambda item=op: click_button(item)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    
# Nút "Xóa toàn bộ" (Clr)
Button(btns_frame, text="Clr", padx=10, pady=10, fg="red",
       command=clear_button).grid(row=5, column=0, columnspan=3, padx=2, pady=2, sticky="ew")

# Nút "="
Button(btns_frame, text="=", padx=10, pady=10, bg="lightblue",
       command=equals_button).grid(row=4, column=3, rowspan=2, padx=2, pady=2, sticky="ns") 
# Lưu ý: Trong ảnh, nút '=' nằm cùng hàng với các phép toán, code này tối ưu bố cục.

root.mainloop()

# --- HẾT CODE MÁY TÍNH BỎ TÚI ---

# --- Khai báo hằng số ---
FILE_NAME = 'NhanVien.xlsx'
COLUMNS = ['Mã', 'Tên', 'Tuổi']

def load_employee_data():
    """Đọc dữ liệu nhân viên từ file Excel."""
    if not path.exists(FILE_NAME):
        print(f"File '{FILE_NAME}' không tồn tại. Tạo DataFrame trống.")
        # Tạo file mới với tiêu đề nếu chưa có
        df_empty = pd.DataFrame(columns=COLUMNS)
        save_employee_data(df_empty, create_new=True) 
        return df_empty
    try:
        # Đọc file Excel. Bỏ qua cột STT nếu có. Header=1 (hàng 2 là tiêu đề), usecols: chỉ lấy cột B, C, D (Mã, Tên, Tuổi)
        df = pd.read_excel(FILE_NAME, header=1, usecols='B:D')
        df.columns = COLUMNS 
        # Chuyển đổi cột Tuổi sang số nguyên
        df['Tuổi'] = pd.to_numeric(df['Tuổi'], errors='coerce').fillna(0).astype(int)
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file Excel: {e}")
        return pd.DataFrame(columns=COLUMNS)

def save_employee_data(df, create_new=False):
    """Lưu DataFrame vào file Excel, đảm bảo định dạng STT."""
    try:
        df_to_save = df.copy()
        # Thêm cột STT tự động (bắt đầu từ 1)
        df_to_save.insert(0, 'STT', range(1, 1 + len(df_to_save)))
        
        # Tạo DataFrame chứa hàng tiêu đề (STT, Mã, Tên, Tuổi)
        header_df = pd.DataFrame(columns=['STT'] + COLUMNS)
        
        with pd.ExcelWriter(FILE_NAME, engine='openpyxl', mode='w') as writer:
            # Ghi tiêu đề vào hàng 1 (startrow=0)
            header_df.to_excel(
                writer, 
                index=False, 
                header=True, 
                startrow=0, 
                sheet_name='Sheet1'
            )
            # Ghi dữ liệu vào từ hàng 2 trở đi (startrow=1)
            df_to_save.to_excel(
                writer, 
                index=False, 
                header=False, 
                startrow=1, 
                sheet_name='Sheet1'
            )
        if not create_new:
             print(f"\n✅ Đã lưu dữ liệu thành công vào '{FILE_NAME}'.")
    except Exception as e:
        print(f"\n❌ Lỗi khi ghi file Excel: {e}")

def add_employee(df):
    """Phần mềm cho phép lưu Nhân viên vào File Excel (Thêm mới)."""
    print("\n--- Thêm Nhân Viên Mới ---")
    ma = input("Nhập Mã nhân viên: ").strip()
    ten = input("Nhập Tên nhân viên: ").strip()
    while True:
        try:
            tuoi = int(input("Nhập Tuổi: ").strip())
            if tuoi >= 0:
                break
            else:
                print("Tuổi phải là số không âm.")
        except ValueError:
            print("Tuổi không hợp lệ. Vui lòng nhập một số nguyên.")

    new_data = pd.DataFrame([{'Mã': ma, 'Tên': ten, 'Tuổi': tuoi}])
    df = pd.concat([df, new_data], ignore_index=True)
    print("✨ Nhân viên đã được thêm vào danh sách.")
    return df

def view_employees(df):
    """Phần mềm cho phép đọc danh sách Nhân viên trong File Excel."""
    print("\n--- Danh Sách Nhân Viên Hiện Tại ---")
    if df.empty:
        print("Danh sách nhân viên hiện đang trống.")
        return
        
    df_display = df.copy()
    df_display.insert(0, 'STT', range(1, 1 + len(df_display)))
    print(df_display.to_string(index=False))

def sort_employees(df):
    """Phần mềm cho phép sắp xếp Nhân viên theo Tuổi tăng dần."""
    if df.empty:
        print("\nDanh sách nhân viên trống. Không thể sắp xếp.")
        return

    df_sorted = df.sort_values(by='Tuổi', ascending=True)
    
    print("\n--- Danh Sách Nhân Viên Sắp Xếp theo Tuổi (Tăng Dần) ---")
    df_display = df_sorted.copy()
    df_display.insert(0, 'STT', range(1, 1 + len(df_display)))
    print(df_display.to_string(index=False))

def run_employee_manager():
    """Chức năng chính của phần mềm Quản lý Nhân viên."""
    employee_df = load_employee_data()
    print("--- 📂 Phần Mềm Quản Lý Nhân Viên (Excel) 🚀 ---")

    while True:
        print("\n\n--- MENU ---")
        print("1. ➕ Thêm (Lưu) nhân viên mới")
        print("2. 📝 Xem danh sách nhân viên")
        print("3. ⬆️ Sắp xếp và hiển thị theo Tuổi tăng dần")
        print("4. 💾 Lưu và Thoát")
        print("5. 🚪 Thoát (Không lưu)")
        
        choice = input("Nhập lựa chọn của bạn (1-5): ")
        
        if choice == '1':
            employee_df = add_employee(employee_df)
        elif choice == '2':
            view_employees(employee_df)
        elif choice == '3':
            sort_employees(employee_df)
        elif choice == '4':
            save_employee_data(employee_df)
            print("Tạm biệt!")
            break
        elif choice == '5':
            print("Không lưu thay đổi. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

# Chạy chương trình Quản lý Nhân viên
# run_employee_manager() # Bỏ comment nếu muốn chạy thử chương trình này