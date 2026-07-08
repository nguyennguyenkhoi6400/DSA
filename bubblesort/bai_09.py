def bubble_sort_b9(a):
    pass_count = 0
    for i in range(len(a)):
        swapped = False
        pass_count += 1
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        # Nếu đi hết 1 lượt j mà không có hoán đổi nào -> mảng đã xếp xong -> thoát
        if not swapped:
            break
    return pass_count

a = [1, 2, 3, 4]
print(bubble_sort_b9(a))