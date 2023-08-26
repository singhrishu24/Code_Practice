'''
Surrounded region : modify the board 
using reverse approach
capture everything except unsurrounded region, i.e not capture border cells
'''

class Solution:
    def solve(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            # for all adjacent cells
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    capture(r, c)
        # 2. capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Uncapture unsurrounded regions (T -> O)    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"