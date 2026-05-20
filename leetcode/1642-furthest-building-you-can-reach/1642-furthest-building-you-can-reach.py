class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        heap = []

        for i in range(len(h) - 1):
            if h[i] >= h[i + 1]:
                continue
            else:
                diff = h[i + 1] - h[i]
                b -= diff
                heappush(heap, -diff)

                if b < 0 and l:
                    b += (-heappop(heap))
                    l -= 1
                
                if b < 0:
                    return i
        
        return len(h) - 1






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna