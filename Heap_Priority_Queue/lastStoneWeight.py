'''
Last Stone Weight
Using Max Heap as we are taking max each time, using min heap to simulate max heap in python
O(n.log(n))
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # as min heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first  = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first # as we are using -ve
            heapq.heappush(stones, first - second)  
        stones.append(0)
        return abs(stones[0])   