'''
N - Queens : n queens to be place on n X n so that they cannot attack each other.
    # we are returning all possible solution
    # queen moves horizontal (EACH IN DIFF ROW),
    # vertical (EACH IN DIFF COL.)and 
    # positive slope dia and -ve slope dia (EACH IN DIFF DIAGONAL)
    # keeping track of Col and +ve and -ve dia using a HashSet
    # for diagonals :
                    i.  for -ve dia (row - col) remains constant
                    ii. for +ve dia (row + col) remains constant
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDia = set() # (r+c)
        nDia = set() # (r-c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range (n):
                if c in col or (r+c) in pDia or (r-c) in nDia:
                    continue

                # Adding Queen    
                col.add(c)
                pDia.add(r+c)
                nDia.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)
                # removing Queen
                col.remove(c)
                pDia.remove(r+c)
                nDia.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return reversed        