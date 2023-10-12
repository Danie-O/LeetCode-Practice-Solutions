class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    if dfs(i, j, grid, rows, cols):
                        island_count += 1

        return island_count

    
def dfs(i, j, grid, rows, cols):
    # check if indices are valid
    if (i < 0 or j < 0 or i >= rows or j >=cols or grid[i][j] == '0'):
        return 0

    grid[i][j] = '0'

    #explore neighboring nodes
    top, left = dfs(i - 1, j, grid, rows, cols), dfs(i, j - 1, grid, rows, cols)
    bottom, right = dfs(i + 1, j, grid, rows, cols), dfs(i, j + 1, grid, rows, cols)

    return (top + left + bottom + right + 1)

        