'''
Word Search : approach it with brute force Recursive BackTracking : DFS
Time Complexity : O(n*m*4^n)
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Base Case
            if i == len(word):
                return True
            # out of bounds conditions
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            # dfs call on all 4 adjacent blocks
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        # calling dfs function     
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # Time Complexity : O(n * m * 4^n)
