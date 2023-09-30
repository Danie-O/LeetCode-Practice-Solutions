def mergeSort(arr):
    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])
    return merge(l, r)


def merge(left, right):
    i, j = 0, 0
    res = []

    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    if i < len(left):
        res.extend(left[i:])
    
    if j < len(right):
        res.extend(right[j:])
    return res

print(mergeSort([5, 1, 7, 3, 2, 8, 6, 4]))