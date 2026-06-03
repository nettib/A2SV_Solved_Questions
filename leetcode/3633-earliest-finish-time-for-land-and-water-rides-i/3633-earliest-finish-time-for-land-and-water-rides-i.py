class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                finish1 = max(
                    waterStartTime[j],
                    landStartTime[i] + landDuration[i]
                ) + waterDuration[j]

                # Water -> Land
                finish2 = max(
                    landStartTime[i],
                    waterStartTime[j] + waterDuration[j]
                ) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna