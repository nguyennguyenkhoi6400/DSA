def day_dai_nhat(array):

    data = set(array)
    longest = 0

    for value in data:

        if value-1 not in data:

            length = 1

            while value+length in data:
                length += 1

            longest = max(longest,length)

    return longest


print(day_dai_nhat([100,4,200,1,3,2]))