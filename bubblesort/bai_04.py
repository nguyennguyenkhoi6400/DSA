def bubble_sort(arr):
    dem = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        dem += 1
    return dem

a = [3, 2, 1]
print(bubble_sort(a))