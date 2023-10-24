def quickSort(array, left_index, right_index):
    if len(array) <= 1: return array
    pivot_index = partition(array, left_index, right_index)

    if left_index < pivot_index - 1:
        quickSort(array, left_index, pivot_index - 1)
    if right_index > pivot_index:
        quickSort(array, pivot_index, right_index)
    
    return array


def partition(items, left_index, right_index):
    pivot = (left_index + right_index) // 2
    pivot = items[pivot]

    l, r = left_index, right_index

    while l <= r:
        while items[l] < pivot:
            l += 1
        while items[r] > pivot:
            r -= 1
        
        if l <= r:
            items[l], items[r] = items[r], items[l]
            l += 1
            r -= 1
        
    # once l > r, we set items[l] as new pivot element.
    return l


a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quickSort(a, 0, len(a) - 1)
print(a)