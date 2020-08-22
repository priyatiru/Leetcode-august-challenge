'''
Easiest approach - rather than checking every element in the intervals(O(n^2)), first sort it is better
to sort intervals because the potential overlapping intervals would be adjacent to one another.

For example consider the sorted array:
[[1,2],[1,3],[2,3],[3,4]]
Start from the beginning,

[[1,2], [1,3]]-> it's obvious these two overlap; would there be any reason to keep [1,3] instead of [1,2]? No. Because it will only decrease the number of intervals we can fit without causing overlaps. So we keep [1,2], aka the interval with the smaller ending.
[[1,2], [2,3]]-> No overlap here, we can keep both. now the "most recent interval" is [2,3]
[[2,3],[3,4]] -> No overlap here, we can keep both. now the "most recent interval" is [3,4]
We can fit 3 intervals without overlap, so we return len(s)-3=4-3=1

'''



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        non_overlaps=0
        recent_interval=intervals[0][0]-1
        for interval in intervals:
            if recent_interval > interval[0]:
                recent_interval= min(recent_interval, interval[1])
            else:
                non_overlaps +=1
                recent_interval=interval[1]
        count_to_remove = len(intervals)-non_overlaps
        return count_to_remove
                