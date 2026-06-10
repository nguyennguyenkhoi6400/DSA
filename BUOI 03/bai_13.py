def bubble_sort_b13(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # So sánh phần tử thứ nhất của cặp (khóa): a[j][0] và a[j+1][0]
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [(2, 'a'), (1, 'b'), (2, 'c')]
print(bubble_sort_b13(a))