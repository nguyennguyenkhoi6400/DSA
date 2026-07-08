def insertion_b3(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] < x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = [5, 2, 4, 6, 1]
print(insertion_b3(a))