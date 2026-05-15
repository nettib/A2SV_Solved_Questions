class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for r in range(len(matrix)):
            heappush(heap, (matrix[r][0], r, 0))
        
        while k:
            num, r, c = heappop(heap)
            k -= 1
            if c + 1 < len(matrix):
                heappush(heap, (matrix[r][c + 1], r, c + 1))
        
        return num


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna