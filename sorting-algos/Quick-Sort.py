def quickSort(array, left_index, right_index):
    if len(items) <= 1: return items

    pivot_index = partition(items, left_index, right_index)
    if left_index < pivot_index - 1:
        quickSort(items, left_index, pivot_index - 1)
    if right_index > pivot_index:
        quickSort(items, pivot_index, right_index)
    
    return items


def partition(items, left_index, right_index):
    pivot = (left_index + right_index) // 2

    l, r = left_index, right_index

    while l <= r:
        while items[l] < items[pivot]:
            l += 1
        while items[r] > items[pivot]:
            r -= 1
        
        if l <= r:
            l, r = items[r], items[l]
            l += 1
            r -= 1
        
    # once l > r, we set items[l] as new pivot element.
    return l


        