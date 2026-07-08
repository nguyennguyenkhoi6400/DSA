import random

def hash_so(key, size):

    a = random.randint(1,10)
    b = random.randint(0,10)
    p = 101

    return ((a*key+b)%p)%size


print(hash_so(20,10))