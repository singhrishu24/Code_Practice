'''
Link : https://leetcode.com/problems/reverse-nodes-in-k-group/
Reverse Nodes in K-Group
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse the group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev 
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next        

    # get to the Kth element
    def getKth(self, curr, k):
        # to do  
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr       