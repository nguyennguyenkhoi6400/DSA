def dem_doan(array, k):

    table = {0:1}
    total = 0
    count = 0

    for value in array:

        total += value

        if total - k in table:
            count += table[total-k]

        table[total] = table.get(total,0) + 1

    return count


print(dem_doan([1,1,1],2))