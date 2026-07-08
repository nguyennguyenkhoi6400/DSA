def shell_sort(arr):

    gap = len(arr) // 2

    while gap > 0:

        for i in range(gap, len(arr)):

            tam = arr[i]
            j = i

            while j >= gap and arr[j-gap] > tam:

                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = tam

        gap //= 2

    print(arr)


shell_sort([9,8,3,7,5,6,4,1])