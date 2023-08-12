'''
Construct Binary Tree from PreOrder and InOrder Traversal
First value in preOrder is always the root.
InOrder : Values to left and right of the root is left and right subTree 

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid  = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid+1 :])
        return root