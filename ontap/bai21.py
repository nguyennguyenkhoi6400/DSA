def kiem_tra(chuoi):

    stack = []

    for ky_tu in chuoi:

        if ky_tu == "(":
            stack.append(ky_tu)

        elif ky_tu == ")":

            if not stack:
                return False

            stack.pop()

    return len(stack) == 0


print(kiem_tra("(()())"))