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

# BFS SOLUTION
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(i, j):
        queue = collections.deque((i, j))
        visited.add((i, j))

        while queue:
            r, c = queue.popleft()

            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and 
                    col in range(cols) and 
                    grid[row][col] == "1" and 
                    (row, col not in visited)):
                    queue.append(row, col)
                    visited.add((row, col))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                islands += 1
    return islands


        