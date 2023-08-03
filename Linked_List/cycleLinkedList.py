'''
Linked List Cycle
Without using HashSet : O(1) Complexity 
Two Pointers : slow(+1) and fast(+2)
Floyd's Tortoise and Hare algorithm.
Fast and Slow pointer will eventually meet will take about (n) iterations.
'''
class Solution:
    def hasCysle(slef, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False    