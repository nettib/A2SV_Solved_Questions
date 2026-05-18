class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            if len(self.heap) == self.k:
                if self.heap[0] < num:
                    heappop(self.heap)
                    heappush(self.heap, num)
            else:
                heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if self.heap[0] < val:
                heappop(self.heap)
                heappush(self.heap, val)
        else:
            heappush(self.heap, val)
        
        return self.heap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna