'''
Reverse Linked List.
Time complexity : O(n), Space Complexity : O(1)
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev    
    

    ''' Improving memory by 0.1 mbs : Removing the temp variable
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 
        return prev    
    '''
