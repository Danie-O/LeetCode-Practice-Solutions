# Ascending order
# def recursiveCounter(low, high):
#     if low == high:
#         return low
#     else:
#         print(low)
#         return recursiveCounter(low + 1, high)

# print(recursiveCounter(0, 6))

# Descending order
def recursiveCounter(low, high):
    if low == high:
        return high
    else:
        print(high)
        return recursiveCounter(low, high - 1)

print(recursiveCounter(0, 6))