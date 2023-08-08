'''
Link : https://leetcode.com/problems/lru-cache/
Least Re-used Cache (LRU) Data Structure.
Functions: Declaring the data structure, Get function : return the value of key,
           put function to add Key value pair/ update the value for key. 
Average Time Complexity : O(1)
Use hashMap to have constant time, # value to be pointer to the node.
Use left and right pointer to keep track of capacity Recently used(Right Pointer) and least recently used (Left pointer).
Using Double Linked List
'''
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashMAp to Key Node

        # Declaring Two Pointers left and right for doubly linked list
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node form list
    # prev <-> node <-> nxt ----> prev <-> nxt
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    # prev <-> nxt --------> prev <-> node <-> right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, prev.prev = nxt, prev

    # defining get function
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # defining put function
    def put(self, key: int, value: int) -> None:
        # update the LRU and Recently used pointers
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])   

        if len(self.cache) > self.cap:
            # remove from the list and delete from the hashMap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]     