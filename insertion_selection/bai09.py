def tim_vi_tri(a, x, left, right):
    while left <= right:
        mid = (left + right) // 2

        if a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left

def insertion_b9(a):
    for i in range(1, len(a)):
        x = a[i]
        vi_tri = tim_vi_tri(a, x, 0, i - 1)
        j = i - 1
        while j >= vi_tri:
            a[j + 1] = a[j]
            j -= 1
        a[vi_tri] = x
    return a

a = [5, 2, 4, 6, 1, 3]
print(insertion_b9(a))