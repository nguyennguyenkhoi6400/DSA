def tinh_hau_to(array):

    stack = []

    for x in array:

        if isinstance(x, int):
            stack.append(x)

        else:

            b = stack.pop()
            a = stack.pop()

            if x == "+":
                stack.append(a + b)

            elif x == "-":
                stack.append(a - b)

            elif x == "*":
                stack.append(a * b)

            elif x == "/":
                stack.append(a // b)

    return stack.pop()


print(tinh_hau_to([2, 3, "+", 4, "*"]))