from tkinter import *
from tkinter import messagebox

# --- HÀM XỬ LÝ SỰ KIỆN ---

def check_password_change():
    """Hàm xử lý khi nhấn nút OK."""
    old_pass = stringOld.get()
    new_pass = stringNew.get()
    re_new_pass = stringReNew.get()
    
    # Giả sử mật khẩu cũ đúng là '123456'
    CORRECT_OLD_PASS = "123456"

    if old_pass == CORRECT_OLD_PASS:
        if new_pass == re_new_pass:
            if new_pass: # Đảm bảo mật khẩu mới không rỗng
                messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
                # Bạn có thể thêm logic lưu mật khẩu mới ở đây
                root.destroy()
            else:
                messagebox.showerror("Lỗi", "Mật khẩu mới không được để trống!")
        else:
            messagebox.showerror("Lỗi", "Mật khẩu mới và Nhập lại mật khẩu không khớp!")
    else:
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")

# --- THIẾT LẬP GIAO DIỆN ---
root = Tk()
root.title("Enter New Password")
root.geometry("300x200")
root.resizable(False, False)

# Khai báo biến StringVar
stringOld = StringVar()
stringNew = StringVar()
stringReNew = StringVar()

# Tạo khung chứa các Label và Entry
input_frame = Frame(root, padx=10, pady=10)
input_frame.pack(padx=10, pady=5)

# 1. Old Password
Label(input_frame, text="Old Password:", anchor='w', width=20).grid(row=0, column=0, pady=5, sticky=W)
Entry(input_frame, textvariable=stringOld, width=20, show="*").grid(row=0, column=1, pady=5)

# 2. New Password
Label(input_frame, text="New Password:", anchor='w', width=20).grid(row=1, column=0, pady=5, sticky=W)
Entry(input_frame, textvariable=stringNew, width=20, show="*").grid(row=1, column=1, pady=5)

# 3. Enter New Password Again
Label(input_frame, text="Enter New Password Again:", anchor='w', width=20).grid(row=2, column=0, pady=5, sticky=W)
Entry(input_frame, textvariable=stringReNew, width=20, show="*").grid(row=2, column=1, pady=5)

# Tạo khung chứa nút
button_frame = Frame(root)
button_frame.pack(pady=10)

# Nút OK
Button(button_frame, text="OK", command=check_password_change, width=10).pack(side=LEFT, padx=10)

# Nút Cancel
Button(button_frame, text="Cancel", command=root.destroy, width=10).pack(side=LEFT, padx=10)

root.mainloop()