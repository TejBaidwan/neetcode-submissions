"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()
        
        l = 0
        rooms = 0

        for i in range(len(ends)):
            if ends[l] > starts[i]:
                rooms += 1
            else:
                l += 1
        
        return rooms







