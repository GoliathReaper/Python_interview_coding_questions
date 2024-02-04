data = ['hippopotamus', 'dog', 'cat', 'lemur', 'fox', 'horse', 'elephant']


def find_len(e):
    return len(e)


data.sort(key=find_len)

print(data[-1])