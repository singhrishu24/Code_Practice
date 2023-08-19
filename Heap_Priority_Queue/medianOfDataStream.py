'''
Find Median from the data stream 
'''

class MedianFinder:
    def __int__(self):
        # initialize the data structure
        # add comments 
        # size of these heaps is approx equal diff ~ 1
        self.small, self.large = [], [] # maxHeap , minHeap
    def addNum(self, num: int) -> None:
        # adding the data streams
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)  

        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.pop)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)   

    def findMedian(self)-> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2