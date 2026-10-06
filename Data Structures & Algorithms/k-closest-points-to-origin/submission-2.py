class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while max_heap:
            _ , x, y = heapq.heappop(max_heap)
            res.append([x , y])

        return res
        