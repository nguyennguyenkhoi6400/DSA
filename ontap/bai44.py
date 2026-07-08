def two_sum(array, target):

    table = {}

    for index, value in enumerate(array):

        if target - value in table:
            return table[target - value], index

        table[value] = index


print(two_sum([2,7,11,15],9))