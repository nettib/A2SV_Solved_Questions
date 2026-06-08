class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        e = []
        g = []

        for num in nums:
            if num < pivot:
                l.append(num)
            elif num > pivot:
                g.append(num)
            else:
                e.append(num)

        ans = []
        ans.extend(l)
        ans.extend(e)
        ans.extend(g)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna