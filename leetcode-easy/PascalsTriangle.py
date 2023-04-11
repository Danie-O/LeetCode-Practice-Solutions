from typing import List

""" Given an integer numRows, return the first numRows of Pascal's triangle.

Note: In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]] # we know that the first level always contains a single number, 1

        for i in range(numRows - 1):
            # add imaginary zeroes to beginning & end of result[-1] to enable us maintain 2 pointers
            # eg: @row 3, temp = [0, 1, 3, 3, 1, 0]
            temp = [0] + result[-1] + [0]
            row = [] # empty array to build next row in the Pascal's triangle

            for j in range(len(result[-1]) + 1):  # the next row is longer than the previous row by 1 element
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result



# Trial:
numRows = 5
s = Solution()
print(s.generate(numRows))
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]