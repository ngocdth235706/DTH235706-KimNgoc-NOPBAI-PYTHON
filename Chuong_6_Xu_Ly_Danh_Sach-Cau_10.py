def input_matrix(name: str, rows: int, cols: int) -> list[list[int]]:
    """Nhập một ma trận từ bàn phím"""
    matrix = []
    print(f"Nhập ma trận {name} ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    val = int(input(f"  {name}[{i}][{j}] = "))
                    row.append(val)
                    break
                except ValueError:
                    print("  Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
        matrix.append(row)
    return matrix

def print_matrix(matrix: list[list[int]], name: str):
    """In ma trận ra màn hình"""
    print(f"\nMa trận {name}:")
    for row in matrix:
        print(" ".join(f"{val:5}" for val in row))

def add_matrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Cộng 2 ma trận A + B"""
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def subtract_matrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Trừ 2 ma trận A - B"""
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def multiply_matrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Nhân 2 ma trận A * B"""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def main():
    try:
        rows = int(input("Nhập số hàng của ma trận: "))
        cols = int(input("Nhập số cột của ma trận: "))
        
        if rows <= 0 or cols <= 0:
            print("Vui lòng nhập số hàng và cột lớn hơn 0.")
            return
        
        # Nhập 2 ma trận
        A = input_matrix("A", rows, cols)
        B = input_matrix("B", rows, cols)
        
        # In các ma trận
        print_matrix(A, "A")
        print_matrix(B, "B")
        
        # Cộng 2 ma trận
        C_add = add_matrices(A, B)
        print_matrix(C_add, "A + B")
        
        # Trừ 2 ma trận
        C_sub = subtract_matrices(A, B)
        print_matrix(C_sub, "A - B")
        
        # Nhân 2 ma trận
        C_mul = multiply_matrices(A, B)
        print_matrix(C_mul, "A * B")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

if __name__ == "__main__":
    main()