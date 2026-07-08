def dem_nghich_the(arr):

    dem = 0

    for i in range(len(arr)):

        for j in range(i+1, len(arr)):

            if arr[i] > arr[j]:
                dem += 1

    return dem


print(dem_nghich_the([2,4,1,3,5]))