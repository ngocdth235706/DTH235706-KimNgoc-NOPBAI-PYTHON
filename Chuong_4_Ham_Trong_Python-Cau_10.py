# Vẽ 4 hình, mỗi hình xuất hiện sau 5 giây

import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

shapes = [
    """\
    *
   * *
  *   *
 *     *
* * * * *
*       *
*       *
""",
    """\
    *
   * *
  *   *
 * * * *
*   *   *
 *     *
  *   *
   * *
    *
""",
    """\
* * * * *
  *   *
   * *
    *
   * *
  *   *
 *     *
* * * * *
""",
    """\
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
]

delay_seconds = 5

def main():
    try:
        for idx, shp in enumerate(shapes, start=1):
            clear_screen()
            print(f"Hình {idx}:\n")
            print(shp)
            if idx < len(shapes):
                print(f"\nChuyển sang hình tiếp theo sau {delay_seconds} giây...")
                time.sleep(delay_seconds)
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình.")

if __name__ == "__main__":
    main()