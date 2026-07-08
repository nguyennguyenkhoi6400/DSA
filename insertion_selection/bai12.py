def insertion_b12(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and len(a[j]) > len(x):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a

a = ['abc', 'a', 'ab']
print(insertion_b12(a))