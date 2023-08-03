'''
Remove Nth element from the end of the Linked List.
using Two pointers left at begining and right shifted n indices
and traverse through the list. Left pointer is at the 
index that needs to be deleted. update the pointer of left to .next.next to delete.
'''
class Solution:
    def removeNthfromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        #deletion
        left.next = left.next.next
        return dummy.next        
