class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        if len(self.large_heap) - len(self.small_heap) == 0:
            if self.small_heap:
                _num = -heappop(self.small_heap) 
                _min = min(num, _num)
                _max = max(num, _num)

                heappush(self.large_heap, _max) 
                heappush(self.small_heap, -_min) 
            else:
                heappush(self.large_heap, num) 
        else:
            _num = heappop(self.large_heap) 
            _min = min(num, _num)
            _max = max(num, _num)

            heappush(self.large_heap, _max) 
            heappush(self.small_heap, -_min) 

    def findMedian(self) -> float:
        m1 = self.large_heap[0]
        if len(self.large_heap) - len(self.small_heap) == 0:
            m2 = -self.small_heap[0]
            return (m1 + m2) / 2
        else:
            return m1
        # m1 = heappop(self.large_heap) 
        # heappush(self.large_heap, m1) 
        # if len(self.large_heap) - len(self.small_heap) == 0:
        #     m2 = -heappop(self.small_heap) 
        #     heappush(self.small_heap, -m2) 
        #     return (m1 + m2) / 2
        # else:
        #     return m1
    

        

# [2, 3, 4, 5, 6, 7, 8, 9]
# [2, 3, 4, 5, 6, 7]

# [2, 3, 4]
# [5, 6, 7]

# [10, 1, 6, 4, 7]

# [1, 4]
# [6, 10]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna