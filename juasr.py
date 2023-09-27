def length(a):
    out = 0
    try:
        while a[out] != a[-1]:
            out += 1
        out += 1
        return out
    except IndexError:
        return 0

class Sort:
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        j = low - 1

        for i in range(low, high):

            if arr[i] <= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]

        arr[j + 1], arr[high] = arr[high], arr[j + 1]
        return j + 1

    @staticmethod
    def quick(arr, low, high):
        if low < high:
            mid = Sort.partition(arr, low, high)
            Sort.quick(arr, low, mid - 1)
            Sort.quick(arr, mid + 1, high)


total = -1
while total != 0:
    array1 = []
    total = int(input('Enter number of students (Enter 0 to exit): '))
    for i in range(total):
         marks = float(input(f'Enter marks of student {i+1}: '))
         array1.append(marks)
    Sort.quick(array1, 0, length(array1)-1)
    print(f"""QUICK SORT
    SORTED ARRAY: {array1}""")



