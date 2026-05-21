"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        for i in range(1, n):
            prev_end = intervals[i - 1].end
            curr_start = intervals[i].start
            if curr_start < prev_end:
                return False
        return True
