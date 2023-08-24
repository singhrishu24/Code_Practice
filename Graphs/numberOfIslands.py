'''
Nuumber of Islands 
map connectd horizontally or vertically i.e neighbors
using bfs approach 
'''
class Solution:
    def numIslands(slef, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r) in range(rows)
                        and (c) in range(cols)
                        and grid[r][c] == '1'
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        def dfs(r, c):
            if(
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c) 
                    islands += 1
                    # or dfs(r, c)
        return islands            