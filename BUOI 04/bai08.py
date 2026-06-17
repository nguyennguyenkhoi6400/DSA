def insertion_b8(a, k):
    for i in range(1, k + 2):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = [4, 3, 2, 1]
k = 1
print(insertion_b8(a, k))