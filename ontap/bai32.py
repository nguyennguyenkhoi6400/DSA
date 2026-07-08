def xoa_so_chan(array):

    index = 0

    while index < len(array):

        if array[index] % 2 == 0:
            array.pop(index)
        else:
            index += 1

    return array


print(xoa_so_chan([1,2,3,4,5,6]))