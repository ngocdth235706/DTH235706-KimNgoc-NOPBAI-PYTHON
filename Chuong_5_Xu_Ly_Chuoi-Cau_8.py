import os
from typing import Tuple

def get_filename_with_ext(path: str) -> str:
    """Trả về tên file kèm phần mở rộng từ đường dẫn."""
    return os.path.basename(path.rstrip('/\\'))

def get_filename_without_ext(path: str) -> str:
    """Trả về tên file (không phần mở rộng) từ đường dẫn."""
    name = get_filename_with_ext(path)
    stem, _ = os.path.splitext(name)
    return stem

def main():
    path = input("Nhập đường dẫn file nhạc (ví dụ d:\\music\\muabui.mp3): ").strip()
    if not path:
        print("Không có đường dẫn nhập vào.")
        return

    file_with_ext = get_filename_with_ext(path)
    file_without_ext = get_filename_without_ext(path)

    print("Tên file (kèm đuôi):", file_with_ext)
    print("Tên file (không đuôi):", file_without_ext)

if __name__ == "__main__":
    main()

import os
from typing import Tuple

def get_filename_with_ext(path: str) -> str:
    """Trả về tên file kèm phần mở rộng từ đường dẫn."""
    return os.path.basename(path.rstrip('/\\'))

def get_filename_without_ext(path: str) -> str:
    """Trả về tên file (không phần mở rộng) từ đường dẫn."""
    name = get_filename_with_ext(path)
    stem, _ = os.path.splitext(name)
    return stem

def main():
    path = input("Nhập đường dẫn file nhạc (ví dụ d:\\music\\muabui.mp3): ").strip()
    if not path:
        print("Không có đường dẫn nhập vào.")
        return

    file_with_ext = get_filename_with_ext(path)
    file_without_ext = get_filename_without_ext(path)

    print("Tên file (kèm đuôi):", file_with_ext)
    print("Tên file (không đuôi):", file_without_ext)

if __name__ == "__main__":
    main()