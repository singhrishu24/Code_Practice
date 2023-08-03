'''
Reorder the Linked List.
Merge first half and second half(reversed)
It has to be reversed as linked list is pointed, could have applied in arrays but not here.
using "First" and "Slow" pointer we can find out the mid of the Linked List.
        Works for the odd valued index even though tne size of the Lists are different.
Merging the list alternating between the two lists, using a temp varible.        
Also the last node will point at null.
'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle of List
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2        