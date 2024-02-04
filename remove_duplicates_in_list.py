
def remove_duplicates(l):
    clean = []
    for i in l:
        if i in clean:
            continue
        else:
            clean.append(i)
    return clean

list_1 = [1, 3, 4, 4, 1, 5, 5, 6]

print(remove_duplicates(list_1))
