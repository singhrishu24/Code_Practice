'''
Find The Duplicate Number : 
    Condition being only 1 element is duplicate ... ever value is in range [1, n] 
    Cycled linked List
    # Floyd's Tortoise and Hare : fast and slow pointers 
    2 * Slow = Fast 
    2(P + C - X)         =  P + 2C - x
    P - X = 0 -> P = X    (P) Preportion of Cycle is always equal to X
'''
class Solution:
    def findDuplicate(self, nums : List[int]) -> int:
        slow , fast = 0, 0 # 0 is not part of the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow        
