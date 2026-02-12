class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed_count = {}

        for num in changed:
            changed_count[num] = changed_count.get(num, 0) + 1

        ans = []
        for num in sorted(changed):
            if num == 0 and changed_count[num] >= 2:
                changed_count[num] -= 2
                ans.append(num)
            elif num != 0 and changed_count[num] != 0 and num * 2 in changed_count and changed_count[num * 2] > 0:
                changed_count[num * 2] -= 1
                changed_count[num] -= 1
                ans.append(num)
        
        if sum(changed_count.values()) == 0:
            return ans
        return []
