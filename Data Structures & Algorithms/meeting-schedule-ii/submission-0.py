"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for interval in intervals:
            events.append((interval.start, 1))   # meeting starts → need room
            events.append((interval.end,  -1))   # meeting ends   → free room

        # Sort by time; at same time, -1 (end) before +1 (start)
        # This handles the (0,8),(8,10) NOT a conflict rule
        events.sort(key=lambda x: (x[0], x[1]))

        max_rooms = 0
        current_rooms = 0

        for time, delta in events:
            current_rooms += delta
            max_rooms = max(max_rooms, current_rooms)

        return max_rooms