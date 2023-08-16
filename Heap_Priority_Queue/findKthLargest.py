'''
Kth Largest Element in an Array : return kth largest in sorted order not kth distinct element
Using MaxHeap which again in python will be minHeap implementation.
Another approach is to use Quick Select Algorithm. Has better avg case complexity : O(n)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums)-1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break
        return nums[k]            

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range (left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        nums[fill], nums[right] = nums[right], nums[fill]
        return fill            

"""
Time and Space complexity happens to be the best in this approach
By simply sorting the array and returning the value.

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
"""

# Implementation using maxHeap approach
# Best Runtime and Memory while running the code on LeetCode

class Solution:
    def findKthLargest(slef, nums: List[int], k : int) -> int:
        heapq.heapify(nums) # make it a max Heap
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]    
