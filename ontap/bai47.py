def hash_chuoi(text):

    p = 31
    mod = 1000000007
    value = 0

    for char in text:

        value = (value*p + ord(char)) % mod

    return value


print(hash_chuoi("hello"))