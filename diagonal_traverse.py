class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        track = {}
        ans = []

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r + c not in track:
                    track[r + c] = []
                track[r + c].append(mat[r][c])

        flag = 1
        for val in track.values():
            if flag:
                ans.extend(val[::-1])
                flag = 0
            else:
                ans.extend(val)
                flag = 1
        
        return ans
