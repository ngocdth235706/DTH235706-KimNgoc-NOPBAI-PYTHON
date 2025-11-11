def display_menu():
    """Hiển thị menu các lựa chọn"""
    print("\n=== XỬ LÝ MẢNG ===")
    print("1. Gộp các số lẻ, tổng cộng có bao nhiêu số lẻ")
    print("2. Gộp các số chẵn, tổng cộng có bao nhiêu số chẵn")
    print("3. Gộp các số nguyên tố")
    print("4. Gộp các số không phải là số nguyên tố")
    print("0. Thoát chương trình")

def is_prime(n):
    """Kiểm tra số n có phải số nguyên tố hay không"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_odd_numbers(M):
    """Lấy các số lẻ từ mảng M"""
    odd_numbers = [num for num in M if num % 2 != 0]
    return odd_numbers

def get_even_numbers(M):
    """Lấy các số chẵn từ mảng M"""
    even_numbers = [num for num in M if num % 2 == 0]
    return even_numbers

def get_prime_numbers(M):
    """Lấy các số nguyên tố từ mảng M"""
    prime_numbers = [num for num in M if is_prime(num)]
    return prime_numbers

def get_non_prime_numbers(M):
    """Lấy các số không phải là số nguyên tố từ mảng M"""
    non_prime_numbers = [num for num in M if not is_prime(num)]
    return non_prime_numbers

def main():
    M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]
    print(f"Mảng M = {M}")
    
    while True:
        display_menu()
        choice = input("Nhập lựa chọn (0-4): ").strip()
        
        if choice == '1':
            odd_nums = get_odd_numbers(M)
            print(f"Dòng 1: Các số lẻ: {odd_nums}, tổng cộng có {len(odd_nums)} số lẻ")
        
        elif choice == '2':
            even_nums = get_even_numbers(M)
            print(f"Dòng 2: Các số chẵn: {even_nums}, tổng cộng có {len(even_nums)} số chẵn")
        
        elif choice == '3':
            prime_nums = get_prime_numbers(M)
            print(f"Dòng 3: Các số nguyên tố: {prime_nums}")
        
        elif choice == '4':
            non_prime_nums = get_non_prime_numbers(M)
            print(f"Dòng 4: Các số không phải là số nguyên tố: {non_prime_nums}")
        
        elif choice == '0':
            print("Thoát chương trình. Tạm biệt!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()