class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))

        _min = intervals[0][0]
        _max = intervals[0][-1]


        n = 1
        for i in range(1, len(intervals)):
            l, r = intervals[i][0], intervals[i][-1]

            if not (_min <= l and _max >= r):
                n += 1
            
            _min = min(_min, l)
            _max = max(_max, r)
        
        return n




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna