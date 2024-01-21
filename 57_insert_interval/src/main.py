from typing import List


def hello():
    return ("Hello")

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        # Is new interval before the first interval? If so, insert it at position 0
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        for i, interval in enumerate(intervals):
            if newInterval[0] == interval[0] and newInterval[1] == interval[1]:
                continue
            # If beginning of new interval is > end of current interval, skip this interval
            if interval[1] < newInterval[0]:
                continue
            # Is interval less than the current interval? Stick it in
            if newInterval[1] < interval[0]:
                if i > 0:
                    if intervals[i-1][0] is not newInterval[0] and intervals[i-1][1] is not newInterval[1]:
                        intervals.insert(i, newInterval)
                        return self.insert(intervals, new_interval)
            
            # Is interval overlapping with current interval? Replace it

            if interval[0] > newInterval[1]:
                continue
            # If beginning of new interval is  <= end of current interval, extend this interval 
            if interval[1] >= newInterval[0]:
                intervals.pop(i)
                if i > 0:
                    if intervals[i-1][0] is not newInterval[0] and intervals[i-1][1] is not newInterval[1]:
                        intervals.insert(i,[min(interval[0], newInterval[0]), max(interval[1],newInterval[1])])
                        newInterval = intervals[i]
                    else:
                        newInterval = [min(interval[0], newInterval[0]), max(interval[1],newInterval[1])]
                        return self.insert(intervals, newInterval)
                else:
                    intervals.insert(0,[min(interval[0], newInterval[0]), max(interval[1],newInterval[1])])
        return intervals


    

if __name__ == "__main__":
    # intervals = [[1,3],[6,9]]
    # new_interval = [2,5]
    # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    # new_interval = [4,8]
    intervals = [[1,2], [7,8]]
    new_interval = [4,5]
    sol = Solution()
    intervals = sol.insert(intervals, new_interval)
    print(intervals)