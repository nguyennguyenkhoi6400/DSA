def bubble_sort_b11(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Hàm abs() dùng để lấy giá trị tuyệt đối trong Python
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [-3, 1, 2, 2]
print(bubble_sort_b11(a))