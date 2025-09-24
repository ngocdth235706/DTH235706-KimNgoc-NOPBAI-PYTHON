import datetime

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

try:
    current_date = datetime.date(year, month, day)
    next_date = current_date + datetime.timedelta(days=1)
    print("Ngày kế tiếp là: {}/{}/{}".format(next_date.day, next_date.month, next_date.year))
except ValueError:
    print("Ngày tháng năm không hợp lệ!")