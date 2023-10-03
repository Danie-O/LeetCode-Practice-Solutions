# Time complexity: 0(n^2)
# Space complexity: O(1)

def bubbleSort(array):
    sorted = False
    largest_index = len(array) - 1

    while not sorted:
        sorted = True
        for i in range(largest_index):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        largest_index -= 1

    return array


print(bubbleSort([65, 55, 45, 35, 35, 25, 15, 10]))