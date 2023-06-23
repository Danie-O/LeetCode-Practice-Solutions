class Solution:
    # USING DYNAMIC PROGRAMMING.
    """
        TIME: O(m*n) ^ 2 => we go over the entire input matrix twice = O((m * n) + (m * n)) times
        SPACE: O(1) => no extra space used besides the few variables to store left, right, top & bottom points     
    ** m = no of rows, n = no of columns
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        MAX = 100000000

        # first pass: left -> right, top -> bottom
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if i - 1 >= 0 else MAX
                    left = mat[i][j - 1] if j - 1 >= 0 else MAX
                    mat[i][j] = min(top, left) + 1
        
        # second pass: bottom -> top, right -> left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if i + 1 < m else MAX
                    right = mat[i][j + 1] if j + 1 < n else MAX
                    mat[i][j] = min(mat[i][j], min(bottom, right) + 1)

        return mat


    # USING BFS. 
    """
         TIME: O(m*n)^2 => 
        - we visit very point in the input matrix (first nested loop), which takes O(m*n) time
        - we also visit every point in the input while iterating over the neighbors of all the points in the queue variable,
          taking O(m * n) time.
        - Together, this is O((m * n) + (m * n))time = O(m * n)^ 2 time

        SPACE: O(m*n) => bcos we create & maintain a new array of visited coordinates = to all points in input
    ** m = no of rows, n = no of columns
    """
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     rows = len(mat)
    #     columns = len(mat[0])
    #     queue = []

    #     for i in range(rows):
    #         for j in range(columns):
    #             if mat[i][j] == 0:
    #                 queue.append((i, j))
    #             else:
    #                 mat[i][j] = '*'
        
    #     for r, c in queue:
    #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #             new_row = dx + r
    #             new_column = dy + c

    #             if 0 <= new_row < rows and 0 <= new_column < columns and mat[new_row][new_column] == '*':
    #                 mat[new_row][new_column] = mat[r][c] + 1
    #                 queue.append((new_row, new_column))

    #     return mat

