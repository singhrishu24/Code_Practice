'''
Invert binary tree. in recursive defination. DFS Search.
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp


        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    '''
        Optimized for memory, not much of difference.
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root   
    '''