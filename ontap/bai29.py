def max_window(array, k):

    result = []

    for i in range(len(array) - k + 1):

        result.append(max(array[i:i+k]))

    return result


print(max_window([1,3,-1,-3,5,3,6,7], 3))