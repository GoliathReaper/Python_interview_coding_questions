def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

# Test the function
nums = [57, 24, 19, 89, 93, 63, 6, 67, 85, 11,
62, 40, 78, 56, 48, 87, 27, 22, 70, 73,
35, 96, 3, 7, 74, 46, 32, 38, 13, 79,
36, 20, 10, 33, 21, 9, 68, 50, 45, 61,
41, 99, 30, 37, 69, 58, 95, 31, 55, 49,
72, 26, 65, 17, 75, 15, 76, 16, 84, 60,
18, 66, 77, 47, 2, 44, 59, 25, 5, 64,
4, 98, 53, 94, 12, 23, 92, 42, 91, 29,
97, 81, 14, 71, 54, 82, 1, 28, 86, 83,
43, 8, 88, 80, 90, 52, 34, 51, 39, 74]
bubble_sort(nums)
print(nums)