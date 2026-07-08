def he_so_tai(size, capacity):

    return size / capacity


size = 8
capacity = 10

load = he_so_tai(size, capacity)

print(load)

if load > 0.75:

    capacity *= 2

print(capacity)