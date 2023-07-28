'''
Longest consecutive Subsequence.
To run at O(n) complexity.

It gets into the while loop only if it is the start of the sequence.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet  = set(nums)
        longest = 0

        for n in nums:
            # Check if it is the start of the sequence.
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest            