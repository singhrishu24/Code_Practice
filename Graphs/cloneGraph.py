'''
Clone Graph : Have to return a deep copy of the graph
Graph is connected and undirected.

class Node: 
    def __init__(self, val = 0, neighbours: None):
        self.val = val
        self.neighbours = neighbours if neighbours no known None else []

Using a HashMap : We map old node to new Nodes
approach is DFS as cloning function
Time Com : O(n) = O(edge + vertices)
'''

class Solution:
    def cloneGraph(self, none: 'Node') -> 'Node':
        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]
            
            copy = Node(node.val)
            oldtoNew[node] = copy
            for nei in node.neighbours:
                copy.neighbours.append(dfs(nei))
            return copy    
        
        return dfs(node) if node else None
        