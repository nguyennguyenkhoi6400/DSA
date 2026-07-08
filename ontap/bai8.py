def bubble_sort_toi_uu(arr):

    so_luot = 0

    for i in range(len(arr)-1):

        da_doi = False
        so_luot += 1

        for j in range(len(arr)-1-i):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]
                da_doi = True

        if not da_doi:
            break

    print("Mảng:", arr)
    print("Số lượt:", so_luot)


bubble_sort_toi_uu([1,2,3,4])