class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key = lambda x: x[1])
        answers = [-1] * len(queries)
        min_heap = []
        i = 0

        for index, q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                # heapq.heappush(min_heap, (size, intervals[i][1]))
                heapq.heappush(min_heap, (size, right))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                answers[index] = min_heap[0][0]
        
        return answers


        # 1. Sort intervals by start
        intervals.sort()

        # 2. Sort queries, but remember their original indexes
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        # 3. Store answers in original query order
        answers = [-1] * len(queries)

        # Heap stores: (interval_size, right)
        # Smallest interval size stays on top
        min_heap = []

        # Pointer for intervals
        i = 0

        # 4. Process queries from smallest to largest
        for index, q in sorted_queries:

            # 5. Add every interval that has started by q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]

                size = right - left + 1

                heapq.heappush(min_heap, (size, right))

                i += 1

            # 6. Remove intervals that ended before q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # 7. Smallest remaining interval contains q
            if min_heap:
                answers[index] = min_heap[0][0]

        return answers
