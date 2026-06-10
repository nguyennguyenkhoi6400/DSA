def bubble_sort_b24(dau, sau):
    a = list(dau)
    dem = 0
    for i in range(len(a)):
        if a == sau:
            break
        dem += 1
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return dem

dau = [4, 3, 2, 1]
sau = [3, 2, 1, 4]
print("Số lượt tối thiểu đã chạy:", bubble_sort_b24(dau, sau))