from typing import List

def characterCount(array: List[str]):
    if len(array) == 1: return len(array[0])

    return len(array[0]) + characterCount(array[1:])
    
print("Testing characterCount():")
print(characterCount(["ab", "c", "def", "ghij"]))
print("============================")


def evenNumbers(array: List[int]):
    res = []
    if len(array) == 1:
        if array[0] % 2 == 0:
            return [array[0]]

    if array[0] % 2 == 0:
        res.append(array[0])
        return res + evenNumbers(array[1:])
    else:
        return evenNumbers(array[1:])

print("Testing evenNumbers():")
print(evenNumbers([3,6,7,99,64,36,0]))
print("============================")


def triangularNumbers(N: int):
    if N <= 0: return 0
    elif N == 1: return 1
    return N + triangularNumbers(N - 1)

print("Testing triangularNumbers():")
print(triangularNumbers(5))
print("=============================")


def firstIndexOfX(word, index = 0):
    if index >= len(word):
        return

    if word[index] == 'x':
        return index
    else:
        return firstIndexOfX(word, index + 1)

print("Testing firstIndexOfX():")
print(firstIndexOfX("abxcdefgx"))
print(firstIndexOfX("abcdefghijklmnopqrstuvwxyz"))
print("=============================")



def shortestUniquePaths(grid: List[list]):
    return 1 + shortestUniquePaths()
    pass