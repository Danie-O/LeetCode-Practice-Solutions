def insertionSort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        # iterate through sorted section of array to find where to 'insert' current unsorted item
        for j in range(i - 1, -1, -1):
            if arr[j] > curr:
                arr[j + 1] = arr[j]     # shift element right to make room for insertion
                arr[j] = curr
    return arr


print(insertionSort([4, -31, 0, 99, 83, -1]), end="----|---")
print(insertionSort([4, -31, 0, 99, 83, 1]))