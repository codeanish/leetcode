from typing import List


def hello():
    return ("Hello")

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Empty
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        # Before start
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        results = []
        for interval in intervals:
            # Interval before new interval
            if interval[1] < newInterval[0]:
                results.append(interval)
                continue
            # New interval overlaps interval
            if newInterval[1] >= interval[0] or interval[1] <= newInterval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1],newInterval[1])]
                if len(results) > 0:
                    latest_result = results.pop()
                    # If results overlap with previous result, discard it, otherwise add it back in
                    if newInterval[0] == latest_result[0]:
                        print("discard previous")
                    else:
                        results.append(latest_result)
                results.append(newInterval)
                continue
            # Interval comes after new interval
            if interval[0] > newInterval[1]:
                if len(results) > 0:
                    latest_result = results.pop()
                    # If results overlap with previous result, discard it, otherwise add it back in
                    if newInterval[0] == latest_result[0]:
                        print("discard previous")
                    else:
                        results.append(latest_result)
                if newInterval not in results:
                    results.append(newInterval)
            results.append(interval)
        last_result = results.pop()
        if newInterval[0] > last_result[1]:
            results.append(last_result)
            results.append(newInterval)
        else:
            results.append(last_result)
        return results
    

if __name__ == "__main__":
    intervals = [[1,2], [7,8]]
    new_interval = [4,5]
    sol = Solution()
    intervals = sol.insert(intervals, new_interval)
    print(intervals)