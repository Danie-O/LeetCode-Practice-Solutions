""" example input: [2,3,3,5]
    expected output: 3 => [2, 3, 5]
"""

def longestIncreasingSubsequence(arr):
    dp = [1] * len(arr)
    l = 0
    prev = 0

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

    # for r in range(1, len(arr)):
    #     l = 0 if arr[r] < arr[prev] else dp[prev]
        
    #     if arr[r] > arr[r - 1]:
    #         dp[r] = max(dp[r], dp[r - 1] + 1)
    #     else:
    #         dp[r] = max(dp[r], l + 1)
    #         prev = r
    # return dp[-1]

print(longestIncreasingSubsequence([0,2,3,3,5]))