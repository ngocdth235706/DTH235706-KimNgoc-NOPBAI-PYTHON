for i in range(1, 11):
    for j in range(2, 6):  # Nhóm 1: từ 2 đến 5
        print(f"{j} x {i:2} = {j*i:2}", end="    ")
    print()

print()  # dòng trống giữa 2 nhóm

for i in range(1, 11):
    for j in range(6, 10):  # Nhóm 2: từ 6 đến 9
        print(f"{j} x {i:2} = {j*i:2}", end="    ")
    print()