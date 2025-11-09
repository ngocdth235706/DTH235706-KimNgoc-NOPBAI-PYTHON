import unicodedata

def is_vowel(ch: str) -> bool:
    """Xác định chữ cái ch có phải nguyên âm (kể cả dấu tiếng Việt) hay không."""
    if not ch.isalpha():
        return False
    # NFD: tách ký tự cơ sở và dấu, ký tự cơ sở đứng đầu
    base = unicodedata.normalize('NFD', ch)[0].lower()
    return base in "aeiouy"

def analyze_text(s: str) -> dict:
    counts = {
        "upper": 0,
        "lower": 0,
        "digits": 0,
        "whitespace": 0,
        "special": 0,
        "vowels": 0,
        "consonants": 0
    }

    for ch in s:
        if ch.isupper() and ch.isalpha():
            counts["upper"] += 1
        if ch.islower() and ch.isalpha():
            counts["lower"] += 1
        if ch.isdigit():
            counts["digits"] += 1
        if ch.isspace():
            counts["whitespace"] += 1
        if not ch.isalnum() and not ch.isspace():
            counts["special"] += 1

        if ch.isalpha():
            if is_vowel(ch):
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1

    return counts

def main():
    s = input("Nhập một chuỗi: ")
    c = analyze_text(s)
    print("Kết quả phân tích:")
    print(" - Chữ IN HOA        :", c["upper"])
    print(" - Chữ in thường     :", c["lower"])
    print(" - Chữ là chữ số     :", c["digits"])
    print(" - Ký tự đặc biệt    :", c["special"])
    print(" - Ký tự khoảng trắng:", c["whitespace"])
    print(" - Nguyên âm         :", c["vowels"])
    print(" - Phụ âm            :", c["consonants"])

if __name__ == "__main__":
    main()