import csv
import random
from typing import List, Tuple

# Tên file CSV
FILE_NAME = 'random_numbers.csv'
NUM_ROWS = 10
NUM_NUMBERS_PER_ROW = 10

def create_random_csv(filename: str, num_rows: int, num_numbers_per_row: int):
    """
    Viết hàm cho phép lưu tập tin dưới dạng CSV file.
    Yêu cầu khởi tạo 10 dòng, mỗi dòng có 10 số ngẫu nhiên bất kỳ
    cách nhau bởi dấu ";".
    """
    print(f"--- 1. Khởi tạo và lưu file '{filename}' ---")
    
    # Mở file để ghi (mode 'w')
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Sử dụng csv.writer và chỉ định dấu phân cách là ';'
        csv_writer = csv.writer(csvfile, delimiter=';')
        
        for i in range(num_rows):
            # Tạo danh sách 10 số ngẫu nhiên từ 0 đến 99
            random_row = [random.randint(0, 99) for _ in range(num_numbers_per_row)]
            
            # Ghi dòng dữ liệu vào file
            csv_writer.writerow(random_row)
            
            # Hiển thị dữ liệu được tạo (chuyển các số thành chuỗi cách nhau bởi ';')
            print(f"Dòng {i+1}: {';'.join(map(str, random_row))}")
            
    print(f"\n✅ Đã tạo thành công {num_rows} dòng vào file '{filename}'.")

def read_and_calculate_sum(filename: str) -> List[Tuple[List[int], int]]:
    """
    Viết hàm cho phép đọc tập tin và xuất ra tổng giá trị của các phần tử
    trên mỗi dòng.
    """
    print(f"\n--- 2. Đọc file '{filename}' và Tính Tổng ---")
    
    results = [] # Lưu trữ (danh sách số trên dòng, tổng của dòng đó)
    
    try:
        # Mở file để đọc (mode 'r')
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # Sử dụng csv.reader và chỉ định dấu phân cách là ';'
            csv_reader = csv.reader(csvfile, delimiter=';')
            
            row_count = 0
            for row_str in csv_reader:
                row_count += 1
                
                # Chuyển đổi các phần tử chuỗi sang số nguyên
                # Loại bỏ các chuỗi rỗng có thể có do lỗi định dạng
                try:
                    numbers = [int(x) for x in row_str if x.strip()]
                    
                    # Tính tổng của dòng
                    total = sum(numbers)
                    results.append((numbers, total))
                    
                    # Xuất kết quả
                    print(f"Dòng {row_count} ({len(numbers)} số): {' '.join(map(str, numbers))}")
                    print(f"  -> Tổng giá trị: {total}")
                    
                except ValueError as e:
                    print(f"❌ Lỗi: Không thể chuyển đổi dữ liệu sang số nguyên ở dòng {row_count}. Chi tiết: {e}")
                    
    except FileNotFoundError:
        print(f"❌ Lỗi: File '{filename}' không được tìm thấy.")
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        
    return results

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == '__main__':
    
    # 1. Thực hiện yêu cầu 1: Tạo và lưu file CSV
    create_random_csv(FILE_NAME, NUM_ROWS, NUM_NUMBERS_PER_ROW)
    
    # 2. Thực hiện yêu cầu 2: Đọc và tính tổng
    read_and_calculate_sum(FILE_NAME)