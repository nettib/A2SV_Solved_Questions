class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        track1 = {}
        lst_idx_sum = float("inf")
        idx = []

        for i, string in enumerate(list1):
            track1[string] = i
        
        for i, string in enumerate(list2):
            if string in track1 and track1[string] + i < lst_idx_sum:
                lst_idx_sum = track1[string] + i
                idx.clear()
                idx.append(i)
            elif string in track1 and track1[string] + i == lst_idx_sum:
                idx.append(i)
        
        ans = []
        for i in idx:
            ans.append(list2[i])

        return ans
