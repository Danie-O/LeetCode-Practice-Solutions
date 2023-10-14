class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board: return False

        rows, cols = len(board), len(board[0])

        # locate first letter
        for i in range(rows):
            for j in range(cols):
                # only call dfs if current cell contains first letter of word
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word):
                        return True
        return False

    
    def dfs(self, i, j, board, word, index = 0):
        if index == len(word): 
            return True

        # check if cell isnt out of bounds of board
        if (i not in range(len(board))) or (j not in range(len(board[0]))):
            return False

        # backtrack if cell doesnt match letter we are looking for or has already been visited
        if board[i][j] != word[index]: 
            return False

        board[i][j] = "#"   # set to non-letter so we cant reuse
        # explore neighboring cells to find next letter
        if (
            self.dfs(i - 1, j, board, word, index + 1) or
            self.dfs(i, j - 1, board, word, index + 1) or
            self.dfs(i + 1, j, board, word, index + 1) or
            self.dfs(i, j + 1, board, word, index + 1)):
            return True
        else: 
            board[i][j] = word[index]


        
        