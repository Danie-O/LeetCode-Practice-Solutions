# Time complexity: 0(n^2)
# Space complexity: O(1)

def selection_sort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


print(selection_sort([33,2,52,106,73]))