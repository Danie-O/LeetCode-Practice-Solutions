# Time complexity: O(m), where m = length of main array
# Space complexity: O(1) because no extra memory is utilised
def isValidSubsequence(array, sequence):
    l = 0
    r = 0
    
    while r < len(array) and l < len(sequence):
        if sequence[l] == array[r]:
            l += 1
        r += 1
    return l == len(sequence)
            
# Time complexity: O(m), where m = length of main array
# Space complexity: O(n) due to new array created, where n = length of subsequence
def isValidSubsequence(array, sequence):
    mySequence = []
    for num in array:
        if num in sequence:
            mySequence.append(num)
        if sequence == mySequence:
            return True
    return False
