import re
from typing import List

def NegativeNumberInStrings(s: str) -> List[int]:
    """
    Trả về danh sách các số nguyên âm (theo thứ tự xuất hiện) tìm được trong chuỗi s.
    Ví dụ: "abc-5xyz-12k9l--p" -> [-5, -12]
    """
    matches = re.findall(r'(?<!\d)-\d+', s)
    return [int(x) for x in matches]

if __name__ == "__main__":
    s = input("Nhập chuỗi: ")
    if not s:
        print("Không có chuỗi nhập vào.")
    else:
        negatives = NegativeNumberInStrings(s)
        if negatives:
            print("Các số nguyên âm trong chuỗi:", negatives)
        else:
            print("Không tìm thấy số nguyên âm trong chuỗi.")