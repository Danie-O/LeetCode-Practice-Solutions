from typing import List
import unittest

# time: O(n), space: O(1)
def maxSumSubarray(array, k):
    """ Find the subarray of size k that has the maximum sum

    Args:
        array (List(int)): list of integers
        k (int): required size of subarray
    """
    start_index = 0
    curr_sum = 0
    max_sum = 0

    for index, value in enumerate(array):
        curr_sum += value

        if index < k:
            max_sum = curr_sum
        else:
            curr_sum -= array[index - k]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_index = index - k + 1

    # return both maxsum subarray and max sum in format; [max_sum_subarray, max_sum]
    return [array[start_index: start_index + k], max_sum]

    # if we were asked to return the max subarray sum of subarrays with size k, we would return the max_sum value


example = [-1, 2, 3, 0, -3, 9]
k = 2
expected_subarray = [-3, 9]
expected_maxsum = 6

class TestMaxSumSubArray(unittest.TestCase):
    def test_max_sum_of_subarray(self):
        self.assertEqual(maxSumSubarray(example, k)[0], expected_subarray, f"expected subarray: {expected_subarray}")

    def test_max_sum(self):
        self.assertEqual(maxSumSubarray(example, k)[1], expected_maxsum, f"expected maxsum == {expected_maxsum}")

if __name__ == '__main__':
    unittest.main()