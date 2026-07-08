def xoa_trung(array):

    result = []

    for value in array:

        if value not in result:
            result.append(value)

    return result


print(xoa_trung([1,2,2,3,1,4]))