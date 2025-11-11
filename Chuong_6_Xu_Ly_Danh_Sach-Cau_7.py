def insert_numbers_in_order(lst: list[int]) -> list[int]:
    """
    Viết chương trình nhập vào một dãy các số theo thứ tự tăng.
    Nếu nhập sai quy cách thì yêu cầu nhập lại.
    In dãy số sau khi đã nhập xong.
    """
    numbers = []
    
    while True:
        try:
            num = int(input("Nhập số (nhập -1 để dừng): "))
            
            if num == -1:
                if len(numbers) == 0:
                    print("Vui lòng nhập ít nhất một số.")
                    continue
                break
            
            # Kiểm tra xem số mới có lớn hơn số cuối cùng không
            if len(numbers) > 0 and num <= numbers[-1]:
                print(f"Lỗi: Số {num} phải lớn hơn số trước đó ({numbers[-1]}). Vui lòng nhập lại.")
                continue
            
            numbers.append(num)
            print(f"Số {num} đã được thêm vào danh sách.")
            
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
            continue
    
    return numbers

def main():
    print("Nhập vào một dãy các số theo thứ tự tăng")
    print("(Nhập -1 để dừng nhập)")
    print()
    
    lst = insert_numbers_in_order([])
    
    print("\nDanh sách số sau khi đã nhập xong:")
    print(lst)

if __name__ == "__main__":
    main()