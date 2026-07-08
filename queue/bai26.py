def max_cua_so_truot(mang_a, k):
    dq_indices = []
    kq = []
    
    for i in range(len(mang_a)):
        if len(dq_indices) > 0 and dq_indices[0] < i - k + 1:
            dq_indices.pop(0)
        while len(dq_indices) > 0 and mang_a[dq_indices[-1]] <= mang_a[i]:
            dq_indices.pop()
        dq_indices.append(i)
        if i >= k - 1:
            kq.append(mang_a[dq_indices[0]])
    return kq

mang_truot = [1, 3, -1, -3, 5, 3]
print("Kết quả cửa sổ k=3:", max_cua_so_truot(mang_truot, 3))