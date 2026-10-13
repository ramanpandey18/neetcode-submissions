class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = defaultdict(int)
        for num in nums:
            visited[num] += 1
        max_heap = []
        for num, freq in visited.items():
            heapq.heappush(max_heap, (-freq, num))
        
        top_k = []
        while max_heap and k:
            freq, num = heapq.heappop(max_heap)
            top_k.append(num)
            k -= 1
        return top_k
