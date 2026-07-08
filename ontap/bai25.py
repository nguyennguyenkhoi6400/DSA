def hinh_chu_nhat(array):

    max_area = 0

    for i in range(len(array)):

        min_height = array[i]

        for j in range(i, len(array)):

            min_height = min(min_height, array[j])

            area = min_height * (j - i + 1)

            if area > max_area:
                max_area = area

    return max_area


print(hinh_chu_nhat([2, 1, 5, 6, 2, 3]))