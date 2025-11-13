import json
import os

# ======= LỚP LỚP HỌC =======
class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop

    def to_dict(self):
        return {"ma_lop": self.ma_lop, "ten_lop": self.ten_lop}

# ======= LỚP SINH VIÊN =======
class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = nam_sinh
        self.ma_lop = ma_lop

    def to_dict(self):
        return {
            "ma_sv": self.ma_sv,
            "ten_sv": self.ten_sv,
            "nam_sinh": self.nam_sinh,
            "ma_lop": self.ma_lop
        }

# ======= LỚP QUẢN LÝ SINH VIÊN =======
class QuanLySinhVien:
    def __init__(self):
        self.lops = []
        self.svs = []
        self.file = "data.json"
        self.doc_file()

    # ===== ĐỌC / GHI FILE JSON =====
    def doc_file(self):
        if os.path.exists(self.file):
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for lop_data in data.get("lops", []):
                    self.lops.append(Lop(**lop_data))
                for sv_data in data.get("sinhviens", []):
                    self.svs.append(SinhVien(**sv_data))

    def luu_file(self):
        data = {
            "lops": [lop.to_dict() for lop in self.lops],
            "sinhviens": [sv.to_dict() for sv in self.svs]
        }
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("💾 Dữ liệu đã được lưu vào file JSON!")

    # ===== QUẢN LÝ LỚP =====
    def them_lop(self):
        ma = input("Nhập mã lớp: ")
        ten = input("Nhập tên lớp: ")
        self.lops.append(Lop(ma, ten))
        print("✅ Thêm lớp thành công!")

    def hien_thi_lop(self):
        print("\n--- DANH SÁCH LỚP ---")
        for lop in self.lops:
            print(f"{lop.ma_lop} - {lop.ten_lop}")

    # ===== QUẢN LÝ SINH VIÊN =====
    def them_sv(self):
        ma = input("Nhập mã sinh viên: ")
        ten = input("Nhập tên sinh viên: ")
        nam = input("Nhập năm sinh: ")
        self.hien_thi_lop()
        ma_lop = input("Nhập mã lớp sinh viên: ")
        self.svs.append(SinhVien(ma, ten, nam, ma_lop))
        print("✅ Thêm sinh viên thành công!")

    def hien_thi_sv(self):
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for sv in self.svs:
            print(f"{sv.ma_sv} - {sv.ten_sv} - {sv.nam_sinh} - Lớp: {sv.ma_lop}")

    def tim_kiem(self):
        tu_khoa = input("Nhập tên sinh viên cần tìm: ").lower()
        ket_qua = [sv for sv in self.svs if tu_khoa in sv.ten_sv.lower()]
        if ket_qua:
            for sv in ket_qua:
                print(f"{sv.ma_sv} - {sv.ten_sv} - {sv.nam_sinh}")
        else:
            print("❌ Không tìm thấy sinh viên!")

    def xoa_sv(self):
        ma = input("Nhập mã sinh viên cần xóa: ")
        for sv in self.svs:
            if sv.ma_sv == ma:
                self.svs.remove(sv)
                print("🗑️ Xóa sinh viên thành công!")
                return
        print("❌ Không tìm thấy sinh viên!")

    def sua_sv(self):
        ma = input("Nhập mã sinh viên cần sửa: ")
        for sv in self.svs:
            if sv.ma_sv == ma:
                sv.ten_sv = input("Nhập tên mới: ")
                sv.nam_sinh = input("Nhập năm sinh mới: ")
                print("✏️ Sửa thông tin sinh viên thành công!")
                return
        print("❌ Không tìm thấy sinh viên!")

    def sap_xep(self):
        self.svs.sort(key=lambda x: x.ten_sv)
        print("✅ Đã sắp xếp sinh viên theo tên (A→Z).")

    # ===== MENU CHÍNH =====
    def menu(self):
        while True:
            print("\n===== QUẢN LÝ SINH VIÊN =====")
            print("1. Thêm lớp")
            print("2. Xem danh sách lớp")
            print("3. Thêm sinh viên")
            print("4. Xem danh sách sinh viên")
            print("5. Tìm kiếm sinh viên")
            print("6. Xóa sinh viên")
            print("7. Sửa sinh viên")
            print("8. Sắp xếp sinh viên theo tên")
            print("9. Lưu file JSON")
            print("0. Thoát")
            chon = input("Chọn: ")

            if chon == "1": self.them_lop()
            elif chon == "2": self.hien_thi_lop()
            elif chon == "3": self.them_sv()
            elif chon == "4": self.hien_thi_sv()
            elif chon == "5": self.tim_kiem()
            elif chon == "6": self.xoa_sv()
            elif chon == "7": self.sua_sv()
            elif chon == "8": self.sap_xep()
            elif chon == "9": self.luu_file()
            elif chon == "0":
                self.luu_file()
                print("👋 Tạm biệt!")
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ!")


# ======== CHẠY CHƯƠNG TRÌNH ========
if __name__ == "__main__":
    app = QuanLySinhVien()
    app.menu()
