class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if right < intervals[i][0]:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                right = max(right, intervals[i][1])
        res.append([left, right])
        return res



class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
