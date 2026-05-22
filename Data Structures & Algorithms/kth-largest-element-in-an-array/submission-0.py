class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)        # push current number

            if len(min_heap) > k:
                heapq.heappop(min_heap)          # evict the smallest

        return min_heap[0]   