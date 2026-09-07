class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        visited = defaultdict(int)

        for num in nums:
            visited[num] += 1
        
        max_priority = []
        for num, freq in visited.items():
            heapq.heappush(max_priority, (-freq, num))
        
        top_k = []
        while k and max_priority:
            freq, num = heapq.heappop(max_priority)
            top_k.append(num)
            k -= 1

        return top_k
        