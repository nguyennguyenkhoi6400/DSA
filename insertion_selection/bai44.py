def selection_b19(a):
    left = 0
    right = len(a) - 1
    while left < right:
        min = left
        max = left
        for i in range(left, right + 1):
            if a[i] < a[min]:
                min = i
            if a[i] > a[max]:
                max = i
        a[left], a[min] = a[min], a[left]
        if max == left:
            max = min
        a[right], a[max] = a[max], a[right]
        left += 1
        right -= 1
    return a

a = [5, 1, 4, 2, 8]
print(selection_b19(a))