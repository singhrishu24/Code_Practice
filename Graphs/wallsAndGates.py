'''
Walls and Gates :
                    -1 representsa a wall
                    0 reps a gate
                    INF i.e. 2147483647 reps an empty room 

            Fill each room with distance to nearest gate. Not return any value.
    # Simultaneous BFS Search from the gate to empty rooms        
'''
class Solutions:
    def walls_and_gates(self, rooms: List[List[int]]):
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        # add room function
        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == rows
                or c == cols
                or (r, c) in visited
                or rooms[r][c] == -1
            ):
                return 
            visited.add((r, c))
            q.append([r, c])
        # find the gates in the grid
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        # increasing layers for empty rooms 
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                # bfs calls
                addRooms(r+1, c)
                addRooms(r-1, c)
                addRooms(r, c+1)
                addRooms(r, c-1)
            dist += 1    