def bubble_sort_b21(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Chỉ so sánh phần tử thứ nhất (key) của cặp: a[j][0] và a[j+1][0]
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [(2, 'X'), (1, 'A'), (2, 'Y'), (1, 'B')]
print(bubble_sort_b21(a))