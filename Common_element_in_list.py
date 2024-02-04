

def common_element(list1, list2):
    exist = []
    for item in list1:
        if item in list2:
            exist.append(item)
    return exist


list1 = [1, 2, 3, 4, 5,]
list2 = [6, 7, 8, 9, 1, 4, 2]

print(common_element(list1, list2))
