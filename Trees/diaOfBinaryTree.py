'''
Diameter of Binary Tree: max distance between two nodes in a binary tree
max length in the tree.
'''
class Solution:
    def diameterOfbinarytree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left, right)
        dfs(root)
        return res