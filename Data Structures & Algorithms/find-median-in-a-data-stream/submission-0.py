# class MedianFinder:

#     def __init__(self):
        

#     def addNum(self, num: int) -> None:
        

#     def findMedian(self) -> float:
        
#     import heapq

class MedianFinder:

    def __init__(self):
        # max heap (invert values to use Python min-heap)
        self.maxHeap = []  # smaller half
        self.minHeap = []  # larger half

    def addNum(self, num: int) -> None:
        # Step 1: insert into correct heap

        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Step 2: balance heaps

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])

        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0   