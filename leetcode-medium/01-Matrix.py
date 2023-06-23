class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])
        queue = []

        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = '*'
        
        for r, c in queue:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = dx + r
                new_column = dy + c

                if 0 <= new_row < rows and 0 <= new_column < columns and mat[new_row][new_column] == '*':
                    mat[new_row][new_column] = mat[r][c] + 1
                    queue.append((new_row, new_column))

        return mat

