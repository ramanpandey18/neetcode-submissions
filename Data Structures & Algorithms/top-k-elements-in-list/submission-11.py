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
        
        
        
        visited = defaultdict(int)
        for num in nums:
            visited[num] += 1
        
        max_heap = []
        for num, freq in visited.items():
            heapq.heappush(max_heap, (-freq, num))
        
        top_k = []
        while max_heap and k:
            freq, num  = heapq.heappop(max_heap)
            top_k.append(num)
            k -= 1
        return top_k


    # First, count the frequency of each number using a hash map. Then, push each (negative frequency, number) pair into a max-heap. Because you use negative frequencies, the most frequent number comes out first.

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
