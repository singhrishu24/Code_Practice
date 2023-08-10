'''
Balanced Binary Tree: Height Balanced
Using recursive DFS 
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return[True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            # left[0] & rigth[0] for balance of left and right node latter for root node
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1+ max(left[1], right[1])]
        return dfs(root)[0]