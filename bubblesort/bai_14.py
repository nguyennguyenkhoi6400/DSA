def bubble_sort_b14(a):
    thap = 0
    cao = len(a) - 1
    while thap < cao:
        # Lượt 1: Đẩy phần tử lớn nhất về cuối mảng (từ trái sang phải)
        for j in range(thap, cao):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        cao -= 1 # Thu hẹp biên phải lại vì phần tử cuối đã đúng chỗ
        # Lượt 2: Đẩy phần tử nhỏ nhất về đầu mảng (từ phải sang trái)
        for j in range(cao, thap, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
        thap += 1 # Thu hẹp biên trái lại vì phần tử đầu đã đúng chỗ      
    return a

a = [5, 1, 4, 2, 8]
print(bubble_sort_b14(a))