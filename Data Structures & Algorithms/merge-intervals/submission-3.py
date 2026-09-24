class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort by start
        # 2. Take the first interval as current merged interval
        # 3. For every next interval:
        #     if overlapping → extend current interval
        #     else           → save current interval and start a new one
        # 4. Return result
        
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            last = result[-1]
            # Overlapping
            if start <= last[1]:
                last[1] = max(last[1], end)
            # Non-overlapping
            else:
                result.append([start, end])
        return result
        