class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]   # Start with first interval
        
        for current in intervals[1:]:
            last = merged[-1]
            
            # If current interval overlaps with last merged interval
            if current[0] <= last[1]:
                # Merge them by taking maximum end
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add as new interval
                merged.append(current)
        
        return merged
        