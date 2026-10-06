class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if first != second:
                remaining = first - second
                heapq.heappush(max_heap, remaining)

        return - max_heap[0] if max_heap else 0
