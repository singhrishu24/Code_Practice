'''
Subsets : return all possible unique subsets of an array.
The order of the subsets does not matter.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            # Base Case
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decision to include the element
            subset.append(nums[i])
            dfs(i+1)

            # decision to NOT include the element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res    