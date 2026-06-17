def insertion_b16(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        print(a[:i + 1])

a = [5, 2, 8, 1]
insertion_b16(a)