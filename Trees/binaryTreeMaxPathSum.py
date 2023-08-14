'''
Bianry Tree max Path Sum : Using DFS Recursive 
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val] # Global Variable

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute max path with split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax) # returning without split
        
        dfs(root)
        return res[0]