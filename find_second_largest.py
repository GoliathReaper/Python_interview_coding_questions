import random


def myfunction():
    return 0.1


def find_largest(list1):
    data = sorted(list1)
    return data[-2]


list1 = list(range(1, 10))


random.shuffle(list1, myfunction)
print(list1)
print(find_largest(list1))
