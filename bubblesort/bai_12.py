def bubble_sort_b12(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Hàm len() dùng để đo độ dài (số ký tự) của chuỗi
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = ['abc', 'a', 'ab']
print(bubble_sort_b12(a))