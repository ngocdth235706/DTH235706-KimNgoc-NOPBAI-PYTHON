def sort_array_descending() -> list:
    """
    Viết chương trình nhập vào một dãy n số thực M[0], M[1], ..., M[n-1],
    sắp xếp dãy số theo thứ tự giảm dần.
    Xuất ra dãy số sau khi đã sắp xếp.
    """
    try:
        n = int(input("Nhập số lượng phần tử n: "))
        
        if n <= 0:
            print("Vui lòng nhập n > 0.")
            return []
        
        M = []
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Nhập M[{i}]: "))
                    M.append(num)
                    break
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số thực hợp lệ.")
        
        # Sắp xếp theo thứ tự giảm dần
        M.sort(reverse=True)
        
        return M
    
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ cho n.")
        return []

def main():
    print("Nhập vào một dãy n số thực và sắp xếp theo thứ tự giảm dần")
    print()
    
    M = sort_array_descending()
    
    if M:
        print("\nDanh sách số sau khi sắp xếp theo thứ tự giảm dần:")
        print(M)

if __name__ == "__main__":
    main()