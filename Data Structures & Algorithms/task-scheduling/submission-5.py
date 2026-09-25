from collections import Counter, deque
import heapq


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        # Max heap: highest frequency first
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

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
        