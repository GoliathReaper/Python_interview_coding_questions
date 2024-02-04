

def bubble_sort(list1):
    sorting = list1
    for i in range(len(list1)):
        try:
            index_1 = list1[i]
            index_2 = list1[i + 1]
            if index_1 < index_2:
                sorting[i] = index_1
                sorting[i + 1] = index_2
            if index_1 > index_2:
                sorting[i] = index_2
                sorting[i + 1] = index_1
        except IndexError:
            pass

    return sorting


list1 = [57, 24, 19, 89, 93, 63, 6, 67, 85, 11,
        62, 40, 78, 56, 48, 87, 27, 22, 70, 73,
        35, 96, 3, 7, 74, 46, 32, 38, 13, 79,
        36, 20, 10, 33, 21, 9, 68, 50, 45, 61,
        41, 99, 30, 37, 69, 58, 95, 31, 55, 49,
        72, 26, 65, 17, 75, 15, 76, 16, 84, 60,
        18, 66, 77, 47, 2, 44, 59, 25, 5, 64,
        4, 98, 53, 94, 12, 23, 92, 42, 91, 29,
        97, 81, 14, 71, 54, 82, 1, 28, 86, 83,
        43, 8, 88, 80, 90, 52, 34, 51, 39, 74]

# everything in the list is less than index_1 < index_2
status = True
while status:
    list1 = bubble_sort(list1)
    print(list1)
    count = 0
    for i in range(len(list1)):
        try:
            index_1 = list1[i]
            index_2 = list1[i + 1]
            if index_1 < index_2:
                count += 1
        except IndexError:
            pass
        if count == len(list1) - 1:
            status = False

