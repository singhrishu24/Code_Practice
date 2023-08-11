'''
Count Good nodes in Binary Tree : good if the path from root to X there are no 
nodes with a value greater than X
Approach the problem using recursive DFS : PreOrder Traversal 
Keeping track of maxValue 
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val) # root node is always a good node