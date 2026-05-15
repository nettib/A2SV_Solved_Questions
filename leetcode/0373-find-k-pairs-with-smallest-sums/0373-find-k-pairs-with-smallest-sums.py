class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while k:
            num, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1

            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna