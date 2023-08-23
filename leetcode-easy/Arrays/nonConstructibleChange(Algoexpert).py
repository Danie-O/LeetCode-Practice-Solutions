# Time: O(n logn), as a result of the sorting operation
# Space: O(1), no extra memory was used

def nonConstructibleChange(coins):        
    coins.sort()
    min_change = 0

    for coin in coins:
        if coin > min_change + 1:
            break
        min_change += coin
        
    return min_change + 1
