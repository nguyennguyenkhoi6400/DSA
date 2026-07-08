def xoay_mang(array, k):

    k %= len(array)

    return array[-k:] + array[:-k]


print(xoay_mang([1,2,3,4,5], 2))