class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        max_heap = [] # Max heap: highest frequency first
        for count in freq.values():
            heapq.heappush(max_heap, -count)

        # (negative_count, available_time)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1
            
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush(max_heap, count)
            
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    cooldown.append((count, time + n + 1))
        return time

        freq = Counter(tasks)

        # Max heap: highest frequency first
        heap = []
        for count in freq.values():
            heapq.heappush(max_heap, -count)

        # (negative_count, available_time)
        cooldown = deque()

        time = 0

        while heap or cooldown:

            time += 1

            # 1. Release tasks whose cooldown is over
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush(heap, count)

            # 2. Execute an available task
            if heap:
                count = heapq.heappop(heap)

                # One occurrence completed
                count += 1

                # 3. Still has occurrences?
                if count < 0:
                    cooldown.append((count, time + n + 1))

        return time
