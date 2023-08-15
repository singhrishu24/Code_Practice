'''
Kth largest element in a Stream : not distinct element
Kth and add function both return Kth largest element.
Use MinHeap of size K : has sorted property 
    add : O(n) search : O(1)
'''
class Kthlargest:
    def __init__(self, k : int, nums : List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:    
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]    