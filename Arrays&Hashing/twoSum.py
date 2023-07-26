'''
Two Sum 
Same Value cannot be used twice.
Only one unique soultion exists.
One pass algo used 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i 

''' "i" is index and "n" is value.'''
