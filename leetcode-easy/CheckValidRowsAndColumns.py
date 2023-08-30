class Solution:
    # Time: O(1), we 
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_set = set()
            col_set = set()

            for j in range(n):
                if (matrix[i][j] < 1 or 
                    matrix[i][j] > n or 
                    matrix[j][i] < 1 or 
                    matrix[j][i] > n):
                    return False

                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])

            if len(row_set) != n or len(col_set) != n:
                return False

        return True
