cases = [
    (3, 5, 7),
    (3, 7, 5),
    (5, 3, 7),
    (5, 7, 3),
    (7, 3, 5),
    (7, 5, 3)
]

for idx, (i, j, k) in enumerate(cases, start=1):
    orig_i, orig_j, orig_k = i, j, k
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"Trường hợp ({chr(96+idx)}): i = {orig_i}, j = {orig_j}, k = {orig_k} => Kết quả: i = {i}, j = {j}, k = {k}")