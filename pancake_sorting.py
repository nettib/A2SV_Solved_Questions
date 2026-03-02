class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []

        for num in range(len(arr), 0, -1):
            k = arr.index(num) + 1

            if k != 1:
                arr[: k] = arr[: k][::-1]
                ans.append(k)
            
            k = num

            if arr.index(num) + 1 != k:
                arr[: k] = arr[: k][::-1]
                ans.append(k)
            
        
        return ans
