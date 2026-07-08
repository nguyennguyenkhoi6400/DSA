bit = [0]*10

def them(word):

    index = hash(word)%10
    bit[index] = 1


def kiem_tra(word):

    index = hash(word)%10
    return bit[index] == 1


them("apple")

print(kiem_tra("apple"))
print(kiem_tra("banana"))