import os

# ======== LỚP DANH MỤC ========
class DanhMuc:
    def __init__(self, ma_danh_muc, ten_danh_muc):
        self.ma_danh_muc = ma_danh_muc
        self.ten_danh_muc = ten_danh_muc

    def __str__(self):
        return f"{self.ma_danh_muc},{self.ten_danh_muc}"


# ======== LỚP SẢN PHẨM ========
class SanPham:
    def __init__(self, ma_sp, ten_sp, don_gia, ma_danh_muc):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.don_gia = float(don_gia)
        self.ma_danh_muc = ma_danh_muc

    def __str__(self):
        return f"{self.ma_sp},{self.ten_sp},{self.don_gia},{self.ma_danh_muc}"


# ======== LỚP QUẢN LÝ ========
class QuanLySanPham:
    def __init__(self):
        self.danhmucs = []
        self.sanphams = []
        self.file_dm = "danhmuc.txt"
        self.file_sp = "sanpham.txt"
        self.doc_file()

    # ======= XỬ LÝ FILE =======
    def doc_file(self):
        if os.path.exists(self.file_dm):
            with open(self.file_dm, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 2:
                        self.danhmucs.append(DanhMuc(*data))
        if os.path.exists(self.file_sp):
            with open(self.file_sp, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        self.sanphams.append(SanPham(*data))

    def luu_file(self):
        with open(self.file_dm, "w", encoding="utf-8") as f:
            for dm in self.danhmucs:
                f.write(str(dm) + "\n")
        with open(self.file_sp, "w", encoding="utf-8") as f:
            for sp in self.sanphams:
                f.write(str(sp) + "\n")

    # ======= DANH MỤC =======
    def them_danh_muc(self):
        ma = input("Nhập mã danh mục: ")
        ten = input("Nhập tên danh mục: ")
        self.danhmucs.append(DanhMuc(ma, ten))
        print("✅ Thêm danh mục thành công!")

    def hien_thi_danh_muc(self):
        print("\n--- DANH MỤC ---")
        for dm in self.danhmucs:
            print(f"{dm.ma_danh_muc} - {dm.ten_danh_muc}")

    # ======= SẢN PHẨM =======
    def them_san_pham(self):
        ma = input("Nhập mã sản phẩm: ")
        ten = input("Nhập tên sản phẩm: ")
        gia = input("Nhập đơn giá: ")
        self.hien_thi_danh_muc()
        ma_dm = input("Nhập mã danh mục của sản phẩm: ")
        self.sanphams.append(SanPham(ma, ten, gia, ma_dm))
        print("✅ Thêm sản phẩm thành công!")

    def hien_thi_san_pham(self):
        print("\n--- DANH SÁCH SẢN PHẨM ---")
        for sp in self.sanphams:
            print(f"{sp.ma_sp} - {sp.ten_sp} - {sp.don_gia} - Danh mục: {sp.ma_danh_muc}")

    def tim_kiem(self):
        tu_khoa = input("Nhập tên sản phẩm cần tìm: ").lower()
        ket_qua = [sp for sp in self.sanphams if tu_khoa in sp.ten_sp.lower()]
        if ket_qua:
            for sp in ket_qua:
                print(f"{sp.ma_sp} - {sp.ten_sp} - {sp.don_gia}")
        else:
            print("❌ Không tìm thấy sản phẩm!")

    def xoa_san_pham(self):
        ma = input("Nhập mã sản phẩm cần xóa: ")
        for sp in self.sanphams:
            if sp.ma_sp == ma:
                self.sanphams.remove(sp)
                print("🗑️ Xóa sản phẩm thành công!")
                return
        print("❌ Không tìm thấy sản phẩm!")

    def sua_san_pham(self):
        ma = input("Nhập mã sản phẩm cần sửa: ")
        for sp in self.sanphams:
            if sp.ma_sp == ma:
                sp.ten_sp = input("Nhập tên mới: ")
                sp.don_gia = float(input("Nhập đơn giá mới: "))
                print("✏️ Sửa sản phẩm thành công!")
                return
        print("❌ Không tìm thấy sản phẩm!")

    def sap_xep(self):
        self.sanphams.sort(key=lambda x: x.don_gia)
        print("✅ Đã sắp xếp sản phẩm theo giá tăng dần.")

    # ======= MENU =======
    def menu(self):
        while True:
            print("\n===== QUẢN LÝ SẢN PHẨM =====")
            print("1. Thêm danh mục")
            print("2. Xem danh mục")
            print("3. Thêm sản phẩm")
            print("4. Xem sản phẩm")
            print("5. Tìm kiếm sản phẩm")
            print("6. Xóa sản phẩm")
            print("7. Sửa sản phẩm")
            print("8. Sắp xếp sản phẩm theo giá")
            print("9. Lưu file")
            print("0. Thoát")
            chon = input("Chọn: ")
            if chon == "1": self.them_danh_muc()
            elif chon == "2": self.hien_thi_danh_muc()
            elif chon == "3": self.them_san_pham()
            elif chon == "4": self.hien_thi_san_pham()
            elif chon == "5": self.tim_kiem()
            elif chon == "6": self.xoa_san_pham()
            elif chon == "7": self.sua_san_pham()
            elif chon == "8": self.sap_xep()
            elif chon == "9": self.luu_file()
            elif chon == "0":
                self.luu_file()
                print("💾 Dữ liệu đã được lưu. Thoát chương trình.")
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ!")


# ======== CHẠY CHƯƠNG TRÌNH ========
if __name__ == "__main__":
    app = QuanLySanPham()
    app.menu()
