import tkinter as tk

def create_button_styles_window():
    # Khởi tạo cửa sổ chính
    window = tk.Tk()
    window.title("frame 2") # Đặt tiêu đề cho cửa sổ

    # Các kiểu dáng (relief) mà chúng ta sẽ sử dụng
    relief_styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]
    # Các độ dày viền (borderwidth) mà chúng ta sẽ sử dụng
    borderwidths = [0, 1, 2, 3, 4]

    # Tạo Frame để chứa các Button (tùy chọn, giúp sắp xếp dễ hơn)
    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack()

    # Thêm nhãn cho cột tiêu đề (borderwidth)
    for i, style in enumerate(relief_styles):
        label = tk.Label(frame, text=style, font=('Arial', 10, 'bold'))
        # Grid: hàng 0, cột i+1 (bắt đầu từ 1 vì cột 0 là nhãn borderwidth)
        label.grid(row=0, column=i + 1, padx=5, pady=5)

    # Lặp qua từng độ dày viền (hàng)
    for r, bw in enumerate(borderwidths):
        # Thêm nhãn cho hàng (giá trị borderwidth)
        bw_label = tk.Label(frame, text=f"borderwidth = {bw}", font=('Arial', 10))
        # Grid: hàng r+1, cột 0 (bắt đầu từ 1 vì hàng 0 là tiêu đề)
        bw_label.grid(row=r + 1, column=0, padx=5, pady=5, sticky='w')

        # Lặp qua từng kiểu dáng (cột)
        for c, relief in enumerate(relief_styles):
            # Tạo Button
            button = tk.Button(
                frame,
                text=relief,
                relief=relief,         # Đặt kiểu dáng của nút
                borderwidth=bw,        # Đặt độ dày viền của nút
                padx=5,
                pady=2
            )
            # Đối với kiểu "solid", chúng ta có thể thêm màu viền để dễ nhìn hơn
            if relief == "solid" and bw > 0:
                button.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
                
            # Đặt Button vào lưới (Grid)
            # Hàng: r+1 (bắt đầu từ 1), Cột: c+1 (bắt đầu từ 1)
            button.grid(row=r + 1, column=c + 1, padx=5, pady=5, sticky='ew')

    # Bắt đầu vòng lặp sự kiện chính của cửa sổ
    window.mainloop()

# Gọi hàm để chạy chương trình
create_button_styles_window()