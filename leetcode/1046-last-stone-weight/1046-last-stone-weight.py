class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): 
            stones[i] = -stones[i]

        heapify(stones) 

        while len(stones) > 1:
            x = -heappop(stones) 
            y = -heappop(stones) 
            rem = abs(x - y)
            if rem: heappush(stones, -rem) 

        return -stones[0] if stones else 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna