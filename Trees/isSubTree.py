'''
Check if a tree is a subtree of another
The idea is to do it with Recursive DFS 
'''
class Solution:
    def isSubTree(self, root: TreeNode, subroot: TreeNode) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subroot):
            return True
        return self.isSubTree(root.left, subroot) or self.isSubTree(root.right, subroot)
    
    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right)
        return False
        