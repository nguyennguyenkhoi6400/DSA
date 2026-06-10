def bubble_sort_b15(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Trường hợp 1: Điểm của người trước thấp hơn người sau, đổi chỗ (giảm dần)
            if a[j][1] < a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]
            # Trường hợp 2: Điểm bằng nhau, so sánh tên theo thứ tự từ điển (tăng dần)
            elif a[j][1] == a[j+1][1]:
                if a[j][0] > a[j+1][0]:
                    a[j], a[j+1] = a[j+1], a[j]
    return a

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(bubble_sort_b15(a))