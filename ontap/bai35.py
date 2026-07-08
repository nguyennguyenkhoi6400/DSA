def gop_doan(array):

    array.sort()

    result = [array[0]]

    for start, end in array[1:]:

        if start <= result[-1][1]:

            result[-1][1] = max(result[-1][1], end)

        else:

            result.append([start, end])

    return result


print(gop_doan([[1,3],[2,6],[8,10],[15,18]]))