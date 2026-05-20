class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Turn the initial list into a valid Min-Heap in-place
        heapq.heapify(self.heap)
        
        # 2. Trim the heap down so it only contains the 'k' largest elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # 2. If the heap exceeds size k, evict the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. The root of the min-heap is now safely the kth largest element
        return self.heap[0]
        
