def insertion_sort(arr):

    dem = 0

    for i in range(1, len(arr)):

        tam = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > tam:

            arr[j+1] = arr[j]
            dem += 1
            j -= 1

        arr[j+1] = tam

    print("Mảng:", arr)
    print("Số lần dịch:", dem)


insertion_sort([3,2,1])