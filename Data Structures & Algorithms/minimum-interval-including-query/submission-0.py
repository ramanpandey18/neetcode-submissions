class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by left endpoint
        intervals.sort()

        # Pair each query with its original index, then sort by value
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        answers = [-1] * len(queries)
        min_heap = []   # (size, right) — min-heap on size
        i = 0           # pointer into sorted intervals

        for orig_idx, q in sorted_queries:

            # 1. Add every interval whose left endpoint <= q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1

            # 2. Evict intervals from heap top whose right endpoint < q
            #    (they don't contain q)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # 3. Heap top is now the smallest interval containing q
            if min_heap:
                answers[orig_idx] = min_heap[0][0]

        return answers