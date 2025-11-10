# Khởi tạo list và biến x
lst = [3, 0, 1, 5, 2]
x = 2

# In kết quả của các phép truy xuất
print("(a) lst[0] =", lst[0])          # 3
print("(b) lst[3] =", lst[3])          # 5
print("(c) lst[x] =", lst[x])          # 1
print("(d) lst[-x] =", lst[-x])        # 1
print("(e) lst[x + 1] =", lst[x + 1])  # 5
print("(f) lst[x] + 1 =", lst[x] + 1)  # 2
print("(g) lst[lst[x]] =", lst[lst[x]]) # lst[1] = 0
print("(h) lst[lst[lst[x]]] =", lst[lst[lst[x]]]) # lst[0] = 3