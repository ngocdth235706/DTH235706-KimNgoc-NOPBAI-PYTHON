import xml.etree.ElementTree as ET
from collections import defaultdict

# --- Khai báo hằng số tên file ---
NHOM_FILE = 'nhomthietbi.xml'
THIETBI_FILE = 'ThietBi.xml'

def load_data():
    """Đọc và tải dữ liệu từ cả hai file XML."""
    nhoms = {}
    thietbis = []
    
    # 1. Đọc danh sách Nhóm Thiết Bị
    try:
        tree_nhom = ET.parse(NHOM_FILE)
        root_nhom = tree_nhom.getroot()
        for nhom_node in root_nhom.findall('nhom'):
            ma = nhom_node.find('ma').text
            ten = nhom_node.find('ten').text
            nhoms[ma] = ten
        print(f"✅ Đã tải {len(nhoms)} nhóm thiết bị từ {NHOM_FILE}.")
    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file {NHOM_FILE}.")
        
    # 2. Đọc danh sách Thiết Bị
    try:
        tree_thietbi = ET.parse(THIETBI_FILE)
        root_thietbi = tree_thietbi.getroot()
        for tb_node in root_thietbi.findall('thietbi'):
            ma_nhom = tb_node.get('manhom') # Đọc thuộc tính manhom
            ma = tb_node.find('ma').text
            ten = tb_node.find('ten').text
            thietbis.append({
                'ma_nhom': ma_nhom,
                'ma': ma,
                'ten': ten
            })
        print(f"✅ Đã tải {len(thietbis)} thiết bị từ {THIETBI_FILE}.")
    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file {THIETBI_FILE}.")
        
    return nhoms, thietbis
def display_nhoms(nhoms):
    """Hiển thị danh sách Nhóm thiết bị."""
    print("\n--- Danh Sách Nhóm Thiết Bị ---")
    if not nhoms:
        print("Danh sách nhóm thiết bị trống.")
        return
        
    print(f"{'Mã Nhóm':<10}{'Tên Nhóm':<20}")
    print("-" * 30)
    for ma, ten in nhoms.items():
        print(f"{ma:<10}{ten:<20}")

def display_all_thietbis(thietbis, nhoms):
    """Hiển thị toàn bộ Thiết bị."""
    print("\n--- Toàn Bộ Danh Sách Thiết Bị ---")
    if not thietbis:
        print("Danh sách thiết bị trống.")
        return

    print(f"{'Mã TB':<10}{'Tên Thiết Bị':<20}{'Mã Nhóm':<10}{'Tên Nhóm':<15}")
    print("-" * 55)
    for tb in thietbis:
        ten_nhom = nhoms.get(tb['ma_nhom'], 'Không rõ') # Lấy Tên Nhóm từ Mã Nhóm
        print(f"{tb['ma']:<10}{tb['ten']:<20}{tb['ma_nhom']:<10}{ten_nhom:<15}")

def filter_thietbis_by_nhom(thietbis, nhoms):
    """Lọc Danh sách Thiết bị theo Nhóm thiết bị."""
    display_nhoms(nhoms)
    
    ma_nhom_can_tim = input("Nhập Mã nhóm thiết bị cần lọc (ví dụ: n1, n2): ").strip().lower()
    
    if ma_nhom_can_tim not in nhoms:
        print(f"Không tìm thấy nhóm thiết bị có mã '{ma_nhom_can_tim}'.")
        return

    nhom_ten = nhoms[ma_nhom_can_tim]
    filtered_list = [tb for tb in thietbis if tb['ma_nhom'] == ma_nhom_can_tim]
    
    print(f"\n--- Danh Sách Thiết Bị của Nhóm '{nhom_ten}' ({ma_nhom_can_tim}) ---")
    if not filtered_list:
        print("Nhóm này hiện không có thiết bị nào.")
        return

    print(f"{'Mã TB':<10}{'Tên Thiết Bị':<20}")
    print("-" * 30)
    for tb in filtered_list:
        print(f"{tb['ma']:<10}{tb['ten']:<20}")

def find_nhom_with_most_thietbis(thietbis, nhoms):
    """Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất."""
    if not thietbis or not nhoms:
        print("\nKhông có đủ dữ liệu để thống kê.")
        return

    # 1. Đếm số lượng thiết bị cho mỗi nhóm
    count_map = defaultdict(int)
    for tb in thietbis:
        count_map[tb['ma_nhom']] += 1
        
    if not count_map:
        print("\nKhông có thiết bị nào được phân loại vào nhóm.")
        return

    # 2. Tìm số lượng lớn nhất
    max_count = max(count_map.values())
    
    # 3. Tìm các nhóm đạt số lượng lớn nhất đó
    most_popular_nhoms = []
    for ma_nhom, count in count_map.items():
        if count == max_count:
            ten_nhom = nhoms.get(ma_nhom, f"Mã không rõ ({ma_nhom})")
            most_popular_nhoms.append((ma_nhom, ten_nhom, count))
            
    # 4. Hiển thị kết quả
    print("\n--- Nhóm Thiết Bị có Số Lượng Thiết Bị Nhiều Nhất ---")
    print(f"Số lượng thiết bị tối đa: {max_count}")
    
    for ma, ten, count in most_popular_nhoms:
        print(f"🏆 Mã: {ma} | Tên: {ten} | Số lượng: {count} thiết bị")
def main():
    """Chức năng chính của phần mềm quản lý thiết bị."""
    
    # Tải dữ liệu khi chương trình khởi động
    nhoms, thietbis = load_data()
    
    while True:
        print("\n==============================")
        print(" Chương Trình Quản Lý Thiết Bị")
        print("==============================")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc Danh sách Thiết bị theo Nhóm")
        print("4. Xuất Nhóm thiết bị có số lượng nhiều nhất")
        print("5. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
        
        if choice == '1':
            display_nhoms(nhoms)
        elif choice == '2':
            display_all_thietbis(thietbis, nhoms)
        elif choice == '3':
            filter_thietbis_by_nhom(thietbis, nhoms)
        elif choice == '4':
            find_nhom_with_most_thietbis(thietbis, nhoms)
        elif choice == '5':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == '__main__':
    main()