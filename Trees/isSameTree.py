'''
Same Tree : root given check if they are the same (structurally, value)
Again we can go to DFS and search recursively 
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right and q.right)
        else:
            return False 