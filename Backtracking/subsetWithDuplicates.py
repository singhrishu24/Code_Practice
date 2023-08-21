'''
Subsets II : set has duplicate values but there can't be duplicate subsets.
As we are not only counting subsets we are not going to use DP.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            # Base Case
            if i == len(nums):
                res.append(subset[::]) # copy
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            # All subsets that don't include nums[i] 
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        backtrack(0, [])
        return res        