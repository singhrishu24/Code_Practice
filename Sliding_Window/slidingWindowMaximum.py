'''
Max Sliding Window: return the max value in the sliding window.
Using Deque. : Time complexity O(n), Memory complexity : O(n)
The queue has to be monolithically decreasing order and conditions are 
to be set in the same manner i.e. value added to accordingly. 
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # index
        l = r = 0
        
        while r < len(nums):
            # pop smaller values from q
            # adding value from the queue 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            # Edge Case : Window atleast size "K"
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output                 