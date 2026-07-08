def selection_sort(arr):

    dem = 0

    for i in range(len(arr)-1):

        nho_nhat = i

        for j in range(i+1, len(arr)):

            dem += 1

            if arr[j] < arr[nho_nhat]:
                nho_nhat = j

        arr[i], arr[nho_nhat] = arr[nho_nhat], arr[i]

    print("Array:", arr)
    print("Số lần so sánh:", dem)


selection_sort([4,2,5,1,3])