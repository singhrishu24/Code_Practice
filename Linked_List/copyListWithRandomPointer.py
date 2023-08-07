'''
Deep Copy of Linked List.
random pointer maybe pointing to node which has not been created yet.
Using Two Loop. Two Passes. Use of HashMap 
'''

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None : None}
        
        cur = head
        # Create a Copy with values
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        # Create a deep copy with next and random pointer
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]        