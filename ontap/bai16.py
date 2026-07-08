def duong_di(parent, end):

    path = []

    while end:

        path.append(end)
        end = parent.get(end)

    path.reverse()

    return path


parent = {
    "A":None,
    "B":"A",
    "C":"A",
    "D":"B"
}

print(duong_di(parent,"D"))