def tim_vi_tri(arr, x, cuoi):

    left = 0
    right = cuoi

    while left <= right:

        center = (left + right) // 2

        if arr[center] < x:
            left = center + 1
        else:
            phai = center - 1

    return left


arr = [1,3,5,7]

print(tim_vi_tri(arr,4,len(arr)-1))