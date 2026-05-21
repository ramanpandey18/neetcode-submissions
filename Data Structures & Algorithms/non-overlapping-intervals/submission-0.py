class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        # Step 1: Sort intervals by end time (earliest ending first)
        intervals.sort(key=lambda x: x[1])
        
        count = 1                    # We can always keep at least 1
        end = intervals[0][1]        # End time of the last kept interval
        
        for i in range(1, len(intervals)):
            # If current interval starts after or at the end of last kept
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]   # Update end time
        
        # Minimum to remove = total - maximum we can keep
        return len(intervals) - count