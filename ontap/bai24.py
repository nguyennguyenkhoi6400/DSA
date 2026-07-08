def next_greater(array):

    stack = []
    result = [-1] * len(array)

    for i in range(len(array) - 1, -1, -1):

        while stack and stack[-1] <= array[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(array[i])

    return result


print(next_greater([2, 1, 3, 5, 4]))