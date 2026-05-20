class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # 2. Smash stones until 1 or 0 stones remain
        while len(max_heap) > 1:
            # Pop the absolute heaviest stone (most negative, sitting at root index 0)
            first_heaviest = heapq.heappop(max_heap) 
            # Pop the second heaviest stone (sitting at the new root index 0)
            second_heaviest = heapq.heappop(max_heap)
            
            # If they are not equal, a new stone is formed with the remaining weight
            if first_heaviest != second_heaviest:
                # E.g., -7 - (-4) = -3 (which represents a stone of weight 3)
                remaining_stone = first_heaviest - second_heaviest
                heapq.heappush(max_heap, remaining_stone)
                
        # 3. If a stone is left, convert it back to positive. Otherwise, return 0.
        return -max_heap[0] if max_heap else 0