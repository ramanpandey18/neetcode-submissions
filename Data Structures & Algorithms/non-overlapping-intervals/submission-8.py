class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for start, finish in intervals[1:]:
            if start >= end:
                end = finish
            else:
                count += 1
        return count 

        # 1. Sort by end time
        intervals.sort(key=lambda x: x[1])

        # 2. Keep the first interval
        end = intervals[0][1]
        removals = 0
        for start, finish in intervals[1:]:
            # 4. No overlap → keep it
            if start >= end:
                end = finish
            # 5. Overlap → remove it
            else:
                removals += 1
        return removals
        
        
        
        
        
        
        # 1. Sort all intervals by END time.

        # 2. Keep the first interval.
        # → Its end becomes our current `end`.

        # 3. Look at every next interval.

        # 4. If current.start >= end:
        #     → No overlap
        #     → Keep this interval
        #     → Update end

        # 5. Otherwise:
        #     → Overlap
        #     → Remove this interval
        #     → Increase removals

        # 6. Return removals.