import pandas as pd
from os import path

# Tên file Excel
FILE_NAME = 'QLNV.xlsx'
# Tên các cột trong DataFrame
COLUMNS = ['Mã', 'Tên', 'Tuổi']

def load_employee_data():
    """Đọc dữ liệu nhân viên từ file Excel."""
    if not path.exists(FILE_NAME):
        print(f"File '{FILE_NAME}' không tồn tại. Tạo DataFrame trống.")
        return pd.DataFrame(columns=COLUMNS)
    try:
        # Đọc file Excel. Bỏ qua cột STT nếu có.
        # header=1 (hàng thứ 2 là tiêu đề), usecols: chỉ lấy các cột B, C, D (Mã, Tên, Tuổi)
        df = pd.read_excel(FILE_NAME, header=1, usecols='B:D')
        
        # Đặt lại tên cột để đảm bảo khớp
        df.columns = COLUMNS 
        
        # Chuyển đổi cột Tuổi sang số nguyên (nếu có thể)
        df['Tuổi'] = pd.to_numeric(df['Tuổi'], errors='coerce').fillna(0).astype(int)
        
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file Excel: {e}")
        return pd.DataFrame(columns=COLUMNS)

def save_employee_data(df):
    """Lưu DataFrame vào file Excel."""
    try:
        # Thêm cột STT tự động (bắt đầu từ 1)
        df.insert(0, 'STT', range(1, 1 + len(df)))
        
        # Lưu vào Excel. index=False để không ghi chỉ mục DataFrame
        # startrow=1 để dữ liệu bắt đầu từ hàng 2, giống như ảnh mẫu (sau tiêu đề)
        # sheet_name='Sheet1' là mặc định
        with pd.ExcelWriter(FILE_NAME, engine='openpyxl', mode='w') as writer:
            # Ghi tiêu đề (Mã, Tên, Tuổi) vào hàng 1
            pd.DataFrame(columns=['STT'] + COLUMNS).to_excel(
                writer, 
                index=False, 
                header=True, 
                startrow=0, 
                sheet_name='Sheet1'
            )
            # Ghi dữ liệu vào từ hàng 2 trở đi
            df.to_excel(
                writer, 
                index=False, 
                header=False, 
                startrow=1, 
                sheet_name='Sheet1'
            )
        print(f"\n✅ Đã lưu dữ liệu thành công vào '{FILE_NAME}'.")
    except Exception as e:
        print(f"\n❌ Lỗi khi ghi file Excel: {e}")

def add_employee(df):
    """Thêm nhân viên mới vào DataFrame."""
    print("\n--- Thêm Nhân Viên Mới ---")
    ma = input("Nhập Mã nhân viên (ví dụ: NV7): ").strip()
    ten = input("Nhập Tên nhân viên: ").strip()
    
    while True:
        try:
            tuoi = int(input("Nhập Tuổi: ").strip())
            if tuoi > 0:
                break
            else:
                print("Tuổi phải là số dương.")
        except ValueError:
            print("Tuổi không hợp lệ. Vui lòng nhập một số nguyên.")

    # Tạo DataFrame mới từ thông tin nhập vào
    new_data = pd.DataFrame([{'Mã': ma, 'Tên': ten, 'Tuổi': tuoi}])
    
    # Nối DataFrame cũ và mới
    df = pd.concat([df, new_data], ignore_index=True)
    print("✨ Nhân viên đã được thêm vào danh sách.")
    return df

def sort_employees(df):
    """Sắp xếp nhân viên theo Tuổi tăng dần."""
    if df.empty:
        print("\nDanh sách nhân viên trống. Không thể sắp xếp.")
        return

    # Sắp xếp theo cột 'Tuổi'
    df_sorted = df.sort_values(by='Tuổi', ascending=True)
    
    print("\n--- Danh Sách Nhân Viên Sắp Xếp theo Tuổi (Tăng Dần) ---")
    # Hiển thị kết quả (thêm cột STT tạm thời cho đẹp)
    df_display = df_sorted.copy()
    df_display.insert(0, 'STT', range(1, 1 + len(df_display)))
    print(df_display.to_string(index=False))

def view_employees(df):
    """Hiển thị toàn bộ danh sách nhân viên hiện tại."""
    print("\n--- Danh Sách Nhân Viên Hiện Tại ---")
    if df.empty:
        print("Danh sách nhân viên hiện đang trống.")
        return
        
    # Hiển thị kết quả (thêm cột STT tạm thời cho đẹp)
    df_display = df.copy()
    df_display.insert(0, 'STT', range(1, 1 + len(df_display)))
    print(df_display.to_string(index=False))


def main():
    """Chức năng chính của phần mềm."""
    # 1. Đọc dữ liệu ban đầu
    employee_df = load_employee_data()
    print("--- 📂 Phần Mềm Quản Lý Nhân Viên (Excel) 🚀 ---")

    while True:
        print("\n\n--- MENU ---")
        print("1. ➕ Thêm nhân viên mới")
        print("2. 📝 Xem danh sách nhân viên hiện tại")
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
            print("Cảm ơn đã sử dụng phần mềm. Tạm biệt!")
            break
        elif choice == '5':
            print("Không lưu thay đổi. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()