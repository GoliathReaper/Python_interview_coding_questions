data = ['hippopotamus', 'cat', 'lemur', 'fox', 'horse', 'elephant', 'dog', 'dog', 'elephant']


def frequency_test(data):
    length = 0
    d = {}
    for i in data:
        k = data.count(i)
        if k >= length:
            length = k
            d[i] = k
            d
    return d


print(frequency_test(data))

