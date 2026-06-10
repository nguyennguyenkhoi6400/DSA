def bubble_sort_b17(a, k):
    # Vòng lặp i chạy đúng k lần ứng với k lượt duyệt
    for i in range(k):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [3, 1, 4, 1, 5]
k = 2
print(bubble_sort_b17(a, k))