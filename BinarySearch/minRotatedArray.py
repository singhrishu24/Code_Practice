'''
Find Min in Rotated sorted Array
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            m = (start + end) // 2
            curr_min = min(curr_min, nums[m])

            if nums[m] > nums[end]:
                start = m + 1
            else:
                end = m - 1
        return min(curr_min, nums[start])             