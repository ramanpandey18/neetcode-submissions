class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:  
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            first_heaviest = heapq.heappop(max_heap)
            second_heaviest = heapq.heappop(max_heap)
            if first_heaviest != second_heaviest:
                remaining_stone = first_heaviest - second_heaviest
                heapq.heappush(max_heap, remaining_stone)
        return -max_heap[0] if max_heap else 0