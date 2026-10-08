class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort by start
        # 2. Take the first interval as current merged interval
        # 3. For every next interval:
        #     if overlapping → extend current interval
                # result[-1][1] = end
        #     else           → save current interval and start a new one
        # 4. Return result
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        end = intervals[0][1]
        for start, finish in intervals[1:]:
            if start <= end:
                end = max(end, finish)
                result[-1][1] = end
            else:
                result.append([start, finish])
                end = finish
        return result

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]
        end = intervals[0][1]

        for start, finish in intervals[1:]:
            # Overlapping
            if start <= end:
                end = max(end, finish)
                result[-1][1] = end
            # Non-overlapping
            else:
                result.append([start, finish])
                end = finish

        return result
        