import mysql.connector

# ⚠️ LƯU Ý: THAY 'MAT_KHAU_ROOT_CUA_BAN' bằng mật khẩu bạn đã đặt
# Tên Database là 'do_an_python' (bạn đã tạo trong Workbench)
config = {
  "host": "localhost",
  "user": "root",
  "password": "DoAn_Python_DH24TH2", 
  "database": "do_an_python" 
}

try:
    mydb = mysql.connector.connect(**config)
    
    if mydb.is_connected():
        print("✅ Kết nối MySQL thành công! Sẵn sàng code!")
        
except mysql.connector.Error as err:
    print(f"❌ Lỗi kết nối MySQL: {err}")
    print("Vui lòng kiểm tra lại mật khẩu Root hoặc trạng thái MySQL Server (port 3306).")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()