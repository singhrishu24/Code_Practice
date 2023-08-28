'''
Pacific Atlantic Water Flow : should flow to both pac and atl
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac , atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return 
            
            visited.add((r, c))
            # calling dfs for all adjacent cells 
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # first row -> Pacific
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c]) # last row -> Atl
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # leftmost column -> Pacific
            dfs(r, COLS - 1, atl, heights[r][COLS-1]) # rightmost column -> Atl

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res                

