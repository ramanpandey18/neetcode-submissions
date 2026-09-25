class MedianFinder:
    def __init__(self):
         # [1,2,3,4,5,6,7] [8,9,10,11,12,13]
        self.max_heap = [] # smaller half
        self.min_heap = [] # larger half

    def addNum(self, num: int) -> None:
        # Step 1: insert into correct heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Step 2: balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0



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