'''
Link : https://leetcode.com/problems/merge-k-sorted-lists/description/
Merge K Sorted Lists : array of sorted linked list needs to be merged in a sorted manner
return a Linked List
# ref to merge two sorted linked list : https://github.com/singhrishu24/Code_Practice/blob/main/Linked_List/mergeTwoLists.py
# use mergeSort 
time complexity O(n.logK)
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = list[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2)) 
            lists = mergedLists
        return lists[0]        
    # implementation of merging two linked lists using mergeSort approach   
    def mergeList(self, l1, l2):
        # to do 
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val< l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next            

